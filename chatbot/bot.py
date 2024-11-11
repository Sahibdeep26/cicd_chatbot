import os
from dotenv import load_dotenv  # Import dotenv package
import slack_sdk
import time

# Load environment variables from .env file
load_dotenv()

# Use the SLACK_API_TOKEN from environment variables
client = slack_sdk.WebClient(token=os.getenv("SLACK_API_TOKEN"))

# Slack channel ID from config
channel_id = os.getenv("SLACK_CHANNEL_ID")

# Function to send a message to the Slack channel
def send_message(message):
    try:
        response = client.chat_postMessage(channel=channel_id, text=message)
        print(f"Message sent: {response['message']['text']}")
    except Exception as e:
        print(f"Error sending message: {e}")

# Simulate pipeline stages with notifications
def start_pipeline():
    send_message("CI/CD pipeline has started!")

def build_success():
    send_message("Build succeeded!")

def build_failure():
    send_message("Build failed!")

def test_results():
    send_message("Tests completed successfully!")

def deployment_success():
    send_message("Deployment succeeded!")

def deployment_failure():
    send_message("Deployment failed!")

def pipeline_complete():
    send_message("CI/CD Pipeline has completed successfully!")

def pipeline_failed():
    send_message("CI/CD Pipeline failed!")

# Simulate the pipeline flow with different stages and notifications
def run_pipeline():
    start_pipeline()
    time.sleep(1)  # Simulate build delay

    # Simulate build success/failure
    build_status = "success"  # Change to "failure" to test build failure
    if build_status == "success":
        build_success()
    else:
        build_failure()
        pipeline_failed()
        return

    time.sleep(1)  # Simulate test delay

    # Simulate test results
    test_status = "success"  # Change to "failure" to simulate test failure
    if test_status == "success":
        test_results()
    else:
        send_message("Tests failed!")
        pipeline_failed()
        return

    time.sleep(1)  # Simulate deployment delay

    # Simulate deployment success/failure
    deployment_status = "success"  # Change to "failure" to simulate deployment failure
    if deployment_status == "success":
        deployment_success()
    else:
        deployment_failure()
        pipeline_failed()
        return

    pipeline_complete()

# Run the pipeline simulation
if __name__ == "__main__":
    run_pipeline()
