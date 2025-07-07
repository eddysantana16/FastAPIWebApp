# tests/e2e/test_e2e.py

import pytest
from playwright.sync_api import expect  # Import Playwright's expect API for better assertions

@pytest.mark.e2e
def test_hello_world(page, fastapi_server):
    """
    Test that the homepage displays "Hello World".
    """
    page.goto('http://localhost:8000')
    expect(page.locator('h1')).to_have_text('Hello World')

@pytest.mark.e2e
def test_calculator_add(page, fastapi_server):
    """
    Test the addition functionality.
    """
    page.goto('http://localhost:8000')
    page.fill('#a', '10')
    page.fill('#b', '5')
    page.click('button:text("Add")')
    expect(page.locator('#result')).to_have_text('Calculation Result: 15')

@pytest.mark.e2e
def test_calculator_subtract(page, fastapi_server):
    """
    Test the subtraction functionality.
    """
    page.goto('http://localhost:8000')
    page.fill('#a', '10')
    page.fill('#b', '5')
    page.click('button:text("Subtract")')
    expect(page.locator('#result')).to_have_text('Calculation Result: 5')

@pytest.mark.e2e
def test_calculator_multiply(page, fastapi_server):
    """
    Test the multiplication functionality.
    """
    page.goto('http://localhost:8000')
    page.fill('#a', '10')
    page.fill('#b', '5')
    page.click('button:text("Multiply")')
    expect(page.locator('#result')).to_have_text('Calculation Result: 50')

@pytest.mark.e2e
def test_calculator_divide(page, fastapi_server):
    """
    Test the division functionality.
    """
    page.goto('http://localhost:8000')
    page.fill('#a', '10')
    page.fill('#b', '5')
    page.click('button:text("Divide")')
    # Accept either "2" or "2.0"
    result_text = page.locator('#result').inner_text()
    assert result_text in ['Calculation Result: 2', 'Calculation Result: 2.0']


@pytest.mark.e2e
def test_calculator_divide_by_zero(page, fastapi_server):
    """
    Test divide by zero edge case.
    """
    page.goto('http://localhost:8000')
    page.fill('#a', '10')
    page.fill('#b', '0')
    page.click('button:text("Divide")')
    expect(page.locator('#result')).to_have_text('Error: Cannot divide by zero!')
