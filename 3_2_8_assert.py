def test_input_text(expected_result, actual_result):
    if expected_result > actual_result or expected_result < actual_result:
        print(f"expected {expected_result}, got {actual_result}")
    else:
        print()
