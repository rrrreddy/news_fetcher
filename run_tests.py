import unittest
import xmlrunner

# Discover and load all the tests in the 'src/tests' directory
test_loader = unittest.TestLoader()
test_suite = test_loader.discover('src/tests')

print(f"Number of tests discovered: {test_suite.countTestCases()}")

# Run the tests and output the results to an XML file
with open('test_results.xml', 'wb') as output:
    test_runner = xmlrunner.XMLTestRunner(output=output)
    result = test_runner.run(test_suite)

# Check the result for success/failure
if result.wasSuccessful():
    print("All tests passed successfully!")
else:
    print("Some tests failed.")

print("Test results have been written to test_results.xml")
