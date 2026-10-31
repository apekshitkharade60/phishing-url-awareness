# Test ResultsPython version used: 3._13.14_ | Operating system: _Windows_______ | Date: _30.10.2026_______
| # | Input | Expected result | Actual result | Pass/Fail |
|---|-------|-----------------|---------------|-----------|
| 1 | https://www.example.com/login | No listed warning signs |No listed warning signs found. THIS DOESNOT PROVE SAFETY. |PASS |
| 2 | http://192.0.2.10/account | IP address + HTTP |- Uses an IP address instead of a familiar domain.
- Uses HTTP. HTTPS alone does not prove trust. | PASS|
| 3 | http://example.com@sample.invalid/login | @ symbol + HTTP |- Contains an @ symbol; inspect carefully.
- Uses HTTP. HTTPS alone does not prove trust. |PASS |
| 4 | https://a.b.c.d.e.example.invalid/path | Many hostname segments | Contains many hostname segments/subdomains.|PASS |
| 5 | https://xn--example.invalid/ | Punycode-style hostname |Contains a punycode-style hostname. | PASS|
## Notes
Basically i learned about some signs and patterns about the harmful or vulnerable URL's . For example if the length of URL is very long it might be suspicious, and URL with HTTP does not assure the safety as it is a protocol to send the data between server and the user.Most important thing is that this project requires very basic setups so it is accessible on maxumum devices.
| Try typing | What happens | What it teaches |
|---|---|---|
| (just press Enter) | No URL entered.[cite: 14] | The program handles empty input.[cite: 14] |
| www.example.com | Uses HTTP. HTTPS alone does not prove trust.[cite: 14] | Missing scheme is treated as http://[cite: 14] |
| https://secure-login.example.invalid | No listed warning signs found.[cite: 14] | A tricky name can slip through. No signs does not mean safe![cite: 14] |
| http://bad | The program stops with ValueError: Invalid IPv6 URL[cite: 14] | A real gap. You will fix it in Section 10 (Improvement C).[cite: 14] | 