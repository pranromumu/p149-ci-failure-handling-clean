def test_failure():
    # Intentional failure!
    assert 1 == 2, "This test is expected to fail to trigger CI failure handling"