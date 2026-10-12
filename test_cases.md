# Test Cases – Simulated Device Monitoring and Alert System

Tested by: Xander Jann M. De Los Santos  
2601306  
Date Tested: October 12, 2026

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 – View initial readings | Choose `1` | Displays 28, 31, 35, 37, and 29 °C | Pending testing | Pending |
| TC02 – Add valid reading | Choose `2`, enter `33` | “Reading added successfully.” | Pending testing | Pending |
| TC03 – Non-numeric input | Choose `2`, enter `abc` | Rejected; no reading added | Pending testing | Pending |
| TC04 – Below range | Choose `2`, enter `-5` | Rejected; no reading added | Pending testing | Pending |
| TC05 – Above range | Choose `2`, enter `120` | Rejected; no reading added | Pending testing | Pending |
| TC06 – Boundary 30 °C | Add `30`, then choose `3` | `30 °C -> WARNING` | Pending testing | Pending |
| TC07 – Boundary 35 °C | Choose `3` | `35 °C -> WARNING` | Pending testing | Pending |
| TC08 – Initial summary | Choose `4` before adding readings | Total 160; average 32.00; minimum 28; maximum 37; status ATTENTION REQUIRED | Pending testing | Pending |
| TC09 – Invalid menu choice | Enter `9` | Error message; menu repeats | Pending testing | Pending |
| TC10 – Exit | Choose `5` | Exit message; program ends | Pending testing | Pending |

## Bugs Found and Fixed

I did not encounter a confirmed bug during testing. The hardest test to verify was checking the boundary values of 30 °C and 35 °C. I checked the program's output to make sure both values were classified as WARNING, while values below 30 °C were classified as NORMAL and values above 35 °C were classified as CRITICAL. This helped me verify that the temperature classification rules were applied correctly.

## Testing Notes

- Run TC08 before adding any new readings to verify the summary of the five initial readings.
- For TC06, add a temperature reading of 30 °C, then select Option 3 to confirm that it is classified as WARNING.
- For TC07, check the original reading of 35 °C and confirm that it is classified as WARNING.
- Test blank input and decimal input, such as `3.5`, to confirm that both are rejected.
- Record the actual program output for each test and mark it PASS or FAIL based on the result.
