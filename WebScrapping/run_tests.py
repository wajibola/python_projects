#!/usr/bin/python
import glob
import sys
from behave import __main__ as runner_main
from datetime import datetime


if __name__ == "__main__":
    sys.stdout.flush()
    feature_file_path = " ./features/feature_files "
    
    result_folder = f"results_{datetime.now().strftime('%y%m%d%H%M')}"

    common_runner_options = (
        f" --no-capture --no-capture-stderr -f allure_behave.formatter:AllureFormatter -o ./allure/{result_folder} "
    )

    runner_options = feature_file_path + common_runner_options
    runner_main.main(runner_options)
