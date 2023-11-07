import allure

from WebTesting.web_access import WebAccess


def before_all(context):
    context.tester = WebAccess()

def after_all(context):
    del context.tester

def before_scenario(context, scenario):
    print(f"Scenario: {scenario.name}")

def after_scenario(context, scenario):
    print(f"Result Scenario: {scenario.status.name} in {round(scenario.duration, 2)}")

def before_feature(context, feature):
    print(f"Feature: {feature.name}")

def after_feature(context, feature):
    print(f"Result Feature: {feature.status.name} in {round(feature.duration, 2)}")

def before_step(context, step):
    print(f"Step: {step.name}")

def after_feature(context, step):
    print(f"Result Step: {step.status.name} in {round(step.duration, 2)}")