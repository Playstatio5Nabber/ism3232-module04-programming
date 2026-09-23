import math

from week5_lab import calculate_order, main


def test_tax_at_seven_percent():
    subtotal, tax, total, _ = calculate_order(2, 100.00)
    assert math.isclose(subtotal, 200.00)
    assert math.isclose(tax, 14.00)
    assert math.isclose(total, 214.00)


def test_over_limit_true():
    _, _, total, requires_approval = calculate_order(3, 450.00)
    assert math.isclose(total, 1444.50)
    assert requires_approval is True


def test_over_limit_false():
    _, _, total, requires_approval = calculate_order(2, 450.00)
    assert math.isclose(total, 963.00)
    assert requires_approval is False


def test_four_data_types():
    product_name = "Laptop"
    quantity = 3
    unit_price = 450.00
    is_over_limit = unit_price * quantity > 1000

    assert isinstance(product_name, str)
    assert isinstance(quantity, int)
    assert isinstance(unit_price, float)
    assert isinstance(is_over_limit, bool)


def test_input_is_converted_to_int(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "2")
    main()
    output = capsys.readouterr().out
    assert "New total for 2 units: $963.00" in output
    assert "Requires approval: False" in output
