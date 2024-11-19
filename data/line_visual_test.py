import pytest
from dash import Dash, dcc, html
from dash.testing.application_runners import import_app

@pytest.fixture
def app_instance():
    app = import_app("line_visual")
    return app

# Test suite
class TestDashApp:

    # Test that the header is present
    def test_001_header_is_present(self, dash_duo, app_instance):
        dash_duo.start_server(app_instance)

        # Assert that the header is present by checking the existence of the element
        dash_duo.wait_for_element("h1", timeout=5)
        assert dash_duo.find_element("h1").text == "Sales Prices of Pink Morsel"

    # Test that the line chart (visualization) is present
    def test_002_visualization_is_present(self, dash_duo, app_instance):
        dash_duo.start_server(app_instance)

        # Assert that the graph exists by checking the Graph component
        dash_duo.wait_for_element("#sales-line-chart", timeout=5)
        assert dash_duo.find_element("#sales-line-chart")

    # Test that the region picker (radio buttons) is present
    def test_003_region_picker_is_present(self, dash_duo, app_instance):
        dash_duo.start_server(app_instance)

        # Assert that the radio items are present by checking the component
        dash_duo.wait_for_element("#region-filter", timeout=5)
        assert dash_duo.find_element("#region-filter")
