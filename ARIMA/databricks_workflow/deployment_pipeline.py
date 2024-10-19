import databricks_cli
from databricks_cli.jobs.api import JobsApi

def deploy_arima_model():
    job_json = 'databricks_workflow/job_config.json'
    jobs_api = JobsApi(None)
    jobs_api.create_from_json(job_json)

if __name__ == "__main__":
    deploy_arima_model()
