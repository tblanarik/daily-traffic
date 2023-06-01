import azure.functions as func
import logging
import os
from message_manager import MessageManager
from wsdot_trafficflow import WSDOTTrafficFlow

app = func.FunctionApp()

@app.function_name(name="ManualRun")
@app.route(route="hello") # HTTP Trigger
def manual_run(req: func.HttpRequest) -> func.HttpResponse:
    """
    This function is used to manually run the traffic report
    """
    traffic_report(2530, debug=True)
    traffic_report(2532, debug=True)
    return func.HttpResponse("Finished checking traffic")

@app.function_name(name="timertrigger")
@app.schedule(schedule="0 30,45 14,23 * * 1-5",
              arg_name="timertrigger",
              run_on_startup=False)
def timer_trigger(timertrigger: func.TimerRequest) -> None:
    traffic_report(2530)
    traffic_report(2532)


def traffic_report(flow_data_id, debug=False):
    """
    This function gets a traffic report and sends an email if there is slow traffic
    """
    access_code = os.environ["WSDOT_ACCESS_CODE"]
    post_url = os.environ["POST_URL"]
    recipients = os.environ["TEXT_RECIPIENTS"]

    traffic_flow = WSDOTTrafficFlow(access_code, flow_data_id)
    message_manager = MessageManager(post_url)

    flow_data = traffic_flow.flow_data()

    if flow_data.flow_reading_value > 1 or debug:
        logging.info("Slow traffic detected: , {flow_data.flow_station_location.description}")
        message_manager.send_message(
            f"{flow_data.flow_station_location.description} Slow Traffic = ({flow_data.flow_reading_value})!",
            recipients)
    else:
        logging.info("No slow traffic: {flow_data.flow_station_location.description}")