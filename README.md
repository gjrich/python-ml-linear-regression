# Why Do We Square Residuals in Linear Regression?

![Why Do We Square Residuals in Linear Regression?](images/why-square-residuals.png)

Try it here: [Comparison App Running in PyShiny](https://shinylive.io/py/app/#code=NobwRAdghgtgpmAXGKAHVA6VBPMAaMAYwHsIAXOcpMAYjvocaeYYB0IaACNTHdlgYMbt+QsS36cAkjFTEATmU4AFKIQDWUAOZwAzpwBiAS3m6yo8ZfoiOK7GQAWpTgGUyUCABMo8z5wAyRgBG8j7YKmqaOrrsRrIKSqFexDCx8YqcZlBkRmZGhDEQAGbyKZxk2KhGEFqccXIZgWZ4nAAqAK6oADZwLQDCUF1dUEE9NlwAogAeFPLQXREa2nqcABQw7WacQXB1EFlDcJ4AlJIAqrq78nAAju0mcPDkuhhkM5JNSqS7qJHLnKg4PJOF1qnBxiousQyF1wkUFHtZmocgA3XaEBw+MiFeoJAFQmHYDBwKaoa66fRQfSoKZpBpKbrQ2EYLShVAOAD6xCCACs4IRsdx9FpiOwSmVGYSWWzOdyeS8OUUjFp2tc6uklMYVdcIcpsC4HNVwr8ltExaUYJlDRBwriMtcvECWtdkUY0eayrprUSSWS9Po7Up7i1qqh2uZiharUaAO5GTw6QWBzgOzxAjmS2EQ-zEQiDTgwYiedo9dX0ySgraDBaOXZkYioAC0PTRCxRPiMIx6lK8nCK7QgAqMpH0Md2EDgRz23HQWGwHst4aMXQDGs4U0rZBa2E3LQ3uTIACZt5vj32B0PSBzd+fBzkrzAeNUtC007pCPIjKh7xAOY-0M+LSJhyuhQoCHIeJ4HLVLMhBwN+4xWEhkgACJwEqE6cAA4lCQT5gAah2XZ6BYSHiBCfQuhQnCePkP5hH2CKeKUqCeMQMYQJwDY-oU-Z3sOv7cQJugcrRAqcAAvJwIDsJwcmcKwYBZOYSAKWAbh+IEQSuO4OR5AUil4LJ8mKRA7SyPOqmKQAcuZeqGcZcmKe+X6WYgakuIQRj2fgjlqcpuiFmmK6Ke5iluNkgVFnAIW+ZxJlKeoPQ+BAoUeV56hGGQjb+HAKUOfFTlgA47Q7PIaXhRlWU5XlcycAAEqVQIFfJalJLoagVepVXZblKWcAASgAgtZLhDX0BUAL6IWR5G2GhGF1g4ux6gaRqcNMfoUpwZxSKRs2CBCFxLSt+repw9xYMsXLfroqzHAWcCOEW5TEJkT3lMt5RZaW7CXb8Og3diqw5DCcASYpADqDjhChb2Q7sLh3D4uwDXo8btIMAacYEE4+INcCsv6AkAPyKacqUQHGjgXUYGC6PGcB4fIqxBFoEO0BMEwGIeBgABzk+5CmFWpx3Ai4MX8jxinC35l2huGIGSwKqx+a1znKxQUFKqYZB-k9TieC1rUJQAsgbL0AIzGybt6XoJ37CaJdFGSLrWXD0ApHBzymKX5FNy3TCt6x7Uuq27CWh17UGXCQXj689RtxbbRXm4nnCHogNsm3x9tA07Ylbmr7ua97iklWVfsiwHIvyxAYYh5r4cp-5pdQd47iXCprst4pfROMQlzcDR2RUk9WfJynMlgNbSCKSho9d5ws89ynimHqF8+Lx9G9gJNq8p1HWsc7P-s2PtB0SLYaOuminB5l0BTC1wZysdkuxQOGKTZPk1bhDGy1OLB30BiDwOgL6XyYBCG+Q474P0ICWH+I5GLAiPlOXO0sIAAAEXSwLgBgeB7A0xFHep7LWioLw-g5Jbe6WcRbXDIKqTiGCBJ-ifDUYAwd6Zt0VCYMwCdDb3QALo2BwXlPBBDBiECIehUhUsjgUP4leQ8tC-IMKYXbKh-4qgcK4WgmO-JSBQXgInYRojcGonwYQx0JDEwAA0ACaqiRZGBIXonhHcx5kHupJKSilZ50Jbuouq+5micB3AePyMVLiBJTsEzioSjwngPBvSmkChCoXQmCTgAAyAmjpgQAHlwwNwgek6wlNqYOFphgYY2BiCKxIF0cy+xVhNI5HGTwjhdASVWAANjwH044xxYlORFlUmpeZfDON7hHOSYiCmvBJBGFuxDHqJxoSM4utt4l9kUiAFhV4hIjmdgKTh9dwzcLIQonW-CTGCOOEI6aYAbAtwWWmeQSz3hzJorIt8H4vybNGS3FMT0NFFH2f8z8jsHzsK0OchuVz5Haz4Xre5RZhHPNktszg7z0yZnnD8tZ75sizAzASTZnBGwAD5DDKlVHAYFLcADkrLOALWyVATRAlPrZFBYwuYlJIRMnCFqBlrLmWvJBXJdFfgpLuOuSi3WAiMUU2lXJKY7Zml6G3Fq9oKwpL2KcWq9VoEGy9ERECOC35JKcGAma8CkFoLkCtfBbxmrBj6t0Lqz1Or1mGxNdKnFrUuCUTytRLlE4Yz4hFZkPMZBZj30xBkcUloGnAk8cG+SSpahSRpPTeNsxm7qtalMCSHrtXeuFiW1q2AJLYD1X6rNtthg7BXBJEAzKpjMvcsyuxzKWjMuwD2zgzKHHMv3tWmtclQY9AkhC9SYFGXSQdYyjAABmIok6pAuvkNasg7kQAwVdd+RAG6t3k22c2zgoapGIOorWUFRMKQ8tBJhTYz4QQHnvikP0gCGakGvVwNGArOIwCmAAam0vCYE4jqlTGnI+hDm5r3XGfQB38b7dhSWAKuzgAAqdcnAIOWr3W6lBRHqjrkbboERPygOcDDe-YeBKv3voZjUAEUxalgh8XHMw8h2gCgRLKjADHjqfV2Dm8VlJPBQTIKEOCPjZUMdUNtKjj6o1sd2GOe+VEpz1m4HJuoShDOPtAYoa9OaMBQDkxyBTag4CrHzVh1YZaK1eu3BJND5IMPXjBMcDAnjgAAAYhGBpNgxkDGjH1irVHKKWr1OAAPfmiYED8VyfVyNywDPzWq7JzY5KVckJmXSmZ4GZa8fl4s+RQb5qzZGypUVsvL8kCv7MOQ7HipyyAIsufopWcdjEWwq48rFlM3mpiBF8lZKc1lQq-M1plcSwV1QXSABbMLfzaOfH1sgSLo6DaMSq0bTyq6zMm5QD55KRU4uJYW-FBJ10+JpXS7UjLr0SvZVkzCXLOu8sSKt-Yw9lAElhG98VrKcXXtlbahVyKjvx1lfda9Hm-UNt9foQ1T1HEo9a3JVdIZd37ttfapdEF47HrI9+NzNGfWVpaLKiLF31U5ttfmklCagTFune5unU7p11oxwzgXNbW3RI7V2kdfaB2juHb28dk7r2tVneDBdLgl2HtXWezd27idusPVT-dOuL1gGZyZfHT7fOsKw7a3DS6CNEZI0b8jMHKMJJo3Rkt1nbPycU05lzvG+eY68z54mV4sOBeC2F83Oygd9mVI5PeeBwDQHgNQa4dwHhPGxK8GY+AiCkAoFQZAvwvBUnYAS9gZkLLsBcnwfYukorBUKC5TK2VkpzGT6n2ACBkBLhXHOAvcdi9kGoOUgQkgB-6CCiWXYjYyx4hgm9Hgc4ykT5mhP4QtgZD0kWFEFYxhdbr-KbqewThOIRXL74AIwRQjyHCKoU0JEIDJgKCiOkeJlIHnyLxKMFQdFahkxPgWgOhuhwQ0kNoZggR5h99lh9B1hNglAdg9gDgegThzgh5M97hrgc8Xg3glBIIv0thJBClMITQD8AQgRtMbBkwa8cAhROB64Fw41XJF8MgApP8OCm8gpokbMqhGDAoWDdAkpaoIAeM8Z5A-xooFhgCwQfA0Z0MBIWhGoypFDfMFAWhhpRpxp1D-QFBN8t8KkuAOVMIXBYBwD2VR5XAnpCgjCoFICF53AbClBrZbBWgYw3pNx9BiASEigoQf5OM5AYImDzIyoq1vgKMEMiDIi3dCVEl3JPhgB-DiBsghE7dLYMAQsWhDwsiWh108jOAAAWQogAVkKL6UKIAHZCi+Ysi6MIkzBEiDxkiAiyB0icNcjLZ8iMAzxKjSiWg6j10WgABODAIoloS2XIvmSYgoqoyYyoooujVCawiWJQVJLgDwrwg8Hwvwtoz9YI8gUImAcIloWIhEaI3sc44EeI08ZoswVo1I9ojIwo3I7IzgAo94ko948o94yo94mo94uosLdgRoo8e43rFItIu3LonovojAAYzgIY0Y8YyY6Y2YjAeY5eELELeo2WNJewtgeaH7KTShG3SJDgQkipGREheg7AfzSQjkMPF9UgVYOxCEx4tI7cDkqE9oh6V7MAnoTkrcPsNooRYFL7CTWyGAPUW-SQgmJQ5wVYfwU2FwY4CVPyOxW1euGzeQUIbANkiLcIKSHUnwfU1YbACLLUk0zAFELIDQVYYAHU74O6HoCAQ044FoOxcLDAVoOSLgIaOTbGWCcjWYVIEWWsZwm0iQwYLQDAaoFENk303FTgOxB6LBVM5MjMwlfLePSMqAYAS2IRFofM0LdIm9AmUDfQQnUjfdGwe7VyBk2qJkwma3Vk9k2-B43k4s8JHksU-k2lQUuAYUlobsiUtlCTTybycIXGWqBUtsziZU1U9UqHEWGsl3b8FoDkLcrc21AKCQ5ku6OxbcCLXZdc-XBCSmYlHgmQkSLDHwFsxU90jspI7s7kzsyE-sqlQczoIU3k0csU8c5lHaIeCKbEXgzLWc-GPQlkxclUtUjUkWa0zIGAGzOzfjdwcgQ0-0zgQMzwYMk9UzIEcM1qCCvc1CwpfwFwC0r0wLJUbxCLc8kMm1KSCCq6UIGAXQQsnsti34DirikE+hePJiwi+s2REQzvTDeQqQw8gSNkvsp4ns7ABStIgctoX84c-80UxSoCkCxGHqGqfqKC4EGCjDNYeClcyVEWMiqSYy0yuSiLNi+i1YU0vUqAA0tMjAckTEQEVYRsbo5eT08JU8+PNikgdCDkMsxnGQ+Mi8vWMSkhCSsQjkCudMWS9slS9o9818r8gUjSkc7StI3SycgyvqOqVQ6g+ypU-wIaFCSyvyGyhqJqeQUyhQe6DAZy1y80zy7ytAJzfyyYoKy0tRUKmK8KooSKsLaK4KWK5i+Kq88S0QlKJkjwDqQgR8hc+Sj84UpSzK8Lb89S8AgqscvySU0C0qsQwaEaMaPoec8POC5cxC0imQ21bQm61qlmOirKFyzAM09yw0ryvQHy-qgKy2IakK0DAsGKvQHIR8esKQghYgCKqKqGmamGuIbIBQDkWawijkBKmiXIbody+zYiVYckEsbEDkwuHstMLyR8LoDMYgGCXQdyGCV8beA9TIBTNS6yb4IClCQmupUFXQCm7GYeGDOGrWcoYiCjLlXQQELyJUQgEeTuJ6J6+SMkGCVYBdVgdgNGEWroQUN3DbDmyaFWrxCeCLTWrC-ZRAAAHkPFKLNpAHtsthC2dtdsPA9rtqmOeQ6oUDhtVjADTkNkMjUlaEqHBHwA8iXTDsUh3TmvJits-BtrAA5nwz6RCwiwluyBAgU1tXWxdodqdudqLrdsmlLs9owA235AxoZsOOxEmi3Urp9tyJrrpsGEZuZqborvO2zQRHJsNunEHsppxVcWFopuAC3lVpUg6Kkk8S7mW1tmtu8RzpDgU39vkEDpHqnuDpG0Uh7J3sUgjsBAPudD0EnvCljrAEPovsNt3oTtEpvuGXxq9HYhAhgBAnMkfAfy2pysUuypaO7J5r5tOtZQFvlqFrTHcGXCnBFpgB-rhARDAub2iTlLnKqogHVrkjsQ6Syk5AwvIrQqggwo8G8TTL8kCmkOCiIcououwC9LwccA5Awq+oYr8hXtWCobYvgcQfuhripOMO+0Wlwo-K4hIVaBhsOu7BP3SWzG-V8Jy32BaDg2HkYUsImWqDXoEhsE638y2Bwz8iDo0lv20jAp-wMmju-30heHvJktbPupaEUngvJgPjWBsjskshaDpKbIfPSogCcbABcbNzceMa8h8haHr3pLsY2scbUmCc9KMfChvJbzDoCggrvOktidgsCYSdCcqiMHb0MrmDSaWrmF8fsafNydVNcaSe6kKeqjKs4gqvKisbKd-FSsqYXMCYGm5CQNqZFjCYad6kurevGlKckpWv2DUGyYwx6b6bMEvQgGWPmjogEgYlWHUDgGwEbEbQBCgD4QekUc6zsM4FNjQGHjfu4JTtqDMy+mRExgWH+zTwgLFDJNhQAk4ykhkhFmcl0jSmsZyAKAkObP8bcdMnMj4FUh8ZibBb8mci8ihfciiYqdmeUPhaUhSeiQBaxZXFRbhd+cSkkoBfafxYcZyYxc6ZJcmc6bRdIHBbAHak6lUiSuWqZfWv8fYGmgWvfGhS0ThVtR+fVkxeyC6j9nUkwu8Bvy0nv3CEBd-xBb8fJYwx8U2BWGSi2F0GRnJCt3uvMuXLExeSNYZbpLFaNelNlLVf0A1aUC1cxh1f8f1bVO2HCFomuAFHBxIFkCXE40fQTKBCHkUcfThs-G43FezgRdcjNYKb1GZWrKbwPOVYukuGtbyk1e1ZWEdaXLVMNfFYZfSdvOjYlcigyeTZWDobWEKV8GqAYj6i2CRntb0Aelh0M0BHkAluHhtcyAzf0CzYstzeNYxdZZKasiNYKaKaafQYUOVZ5StZBDTdtZ7d1dgqdcC3DcniKipdHfFanInbELjaarUOVYRDndKCCCQOXbMomS5S9aCBrZ-HEe7cbb8ChG2jd2qFBADe4F7BGF0GIGaWolff0DdwaRhCMADcZygEyk4yynne2kuH2CyjdDrDelA8-dMF5RxlVIHYjcZdWuZbCjHfqb3ZSgPbGb6A+rLd7YWcByfOS3wdwqCD-YA92DQhRE7B-BDCREsXB3ov0GDZkJaCINwOIDRB8PDHQ6rUfGg6AIZCxHyEQXkHB3QiKClmQ4owXtsPo5pkfBtC4gk-A9MBw5eQgG5ZpLtSehAnJydQ3PIb2sAa7LFMZxG2Re5oOqHOOsArAeAuUFKHY7TEufqFLH+0cD5TjCGCoPbYDskyTUHkoH9RelWDloU2fEC2wYLGyAxAS88CXvvjHn8n+bnktzPN0gsdsayf8bZJPJxTzCHghdryK5LV2RhYq5nfbOq5+Vq92EjaRdQ2EsReida6fKq+Cpq-y7+ZLcLca-VRK8m5bzJeG+PNG86-G6JbEM3mK+EtJdhba+fI65bi67Ui3dy9zMhuHY6earpb2+W4O9W-ZY26a628mfZau5G+GpW6Hg5BO7awOaHkIm1QmD1LaoXTOAgHUAgHYjAxc+kllWeRrjWWAk2x-HWGh4EzUoE10qwg+iR55Tdy0GQ6h8TgwHS7hqy9lVy8O4m5Um+7kl2UUlptabG7q8gEhbcj68hrUgZ77ttkp6UgG4e5m-j05-5EZ4++65FfAqm5p-5Q0WF4-G55Nl5-O4F+lTp7AC55M9u+Z+O-Z9l-p5F4V9al5-u+m9V6F-1-l815TkO6+9Q1+92H+-1UB9KBZhB7B4h44my8PVh6WfPkpMEckD6CMSQ9IHzGmH5CXGcFkcgVoJIQ5A5Befj98TUnj8fGqHj4278kEboCz+kBIV00E04kcGy1n1LCpEuYBU3MkyL6kfTSUcKBDTOag92BFrVFrCHhOeSwUHUB-T1KlizBFi4B2Bg12EDE-Xb9JKUWB2X2-ehGWmBFL-wSz+z+KwrP1tFuINMzejMAUF2FUZHsYK5ULnWYfxGoNsFBwxWcb4GgHE4FUf+yIJ37VBHuA4RCcK5TWOXj8jdxedHIvGc-ThUY9Gm4XLiJWpxKApIucNzDeDBKx4J6htF4DwCuyrBp4IdIsGlF-7h1I6aUWVIEw1zmoAWS6QJo-XAFpRbOgTd-l3C6izxJoNca-rf3v7vNOIj-eGlcDvpG03+qxHeN-wRCYDc4AAw2NOGAEHhQBRA2suRkgEXhoBKSZJGYEPBwCX+-BQEF4BQGKQ0BScdyJgOPrYDVIuAmOgQJZZiD46cVMgXFQoEc0uou8Wgavy4CQxPw1EF-klj6AuB8ICeMYOMgY7mp3SikHbk+RbLn8Xg7+OOmABjBh0o0WGDmOTEYLv4lQPQXLkqBiieAXmWOTgLvXUHBCT6UdPAdfWIEmDo609LxAfRxQxh7B1BKSO-gwAC0BQdgrKNzhiGwNRy4HLoEkN7w9IEhzQ5IXQJTglDahnyHoRQGWi2ZuccA-odNlGGlAYwd0F-l0JwoQMia4QR9I4PL5cp3AowHTAxz5i-IO6CwBuq-1QQO4iCtnPyLREgbE1VhPQMmuwKrQzE1Is8CLCcPmEk01hlwgIYMUCa7wZhFZPCiH1gLQMDm6BTIN-QYipodIc3NBhwxTreI-Y7ANCDAwBEuAgRD+CjCg1LbGU7qK7VYJQI+hg1LalDJwDGA-pf0EGYQaQWElgGr9OG0IiALCP+FTgERxIpEW7hRG3kp2JlXbmsCxHrEtkZuPEe-Soa8MSRiSM8GCXkF7whEQAA)

This repo (python-ml-linear-regression) is for exploring simple linear regression using Python (and PyShiny).

## Explore the PyShiny Playground

We use the Shiny for Python (PyShiny) online playground to explore. 

- PyShiny https://shiny.posit.co/py/
- Playground https://shinylive.io/py/examples/
- Plotly Example: https://shinylive.io/py/examples/#plotly

Go to the Plotly Example at the link above. 
Notice there are two code files:

- app.py (visible tab)
- requirements.txt (background tab)

Click the run arrow to see the current chart.

We can use PyShiny to explore linear regression using Python. 

## Example 1: Random Linear Regression

Go to the PyShiny Playground. 
Run the [Plotly Example](https://shinylive.io/py/examples/#plotly).

For this example, we need to edit one file:

 - We'll replace the code in the app.py in the Playground with our **app_random.py** code.

### app.py

This Repo: Click on app_random.py above. Select all the code (CTRL A if Windows or CMD A if Mac). 
Copy the code to your clipboard (CTRL C if Windows, or CMD C if Mac). 

Browser: Click in the Playgroud app.py tab. Select all the code in the app.py playground example (CTRL A if Windows or CMD A if Mac). 
Paste the code from your clipboard (app_random.py as shown in this repo) into app.py in the Playground (CTRL V if Windows, or CMD V if Mac).
Verify the code copied correctly. 

Click the run arrow (⏵) to see the updated app. 

## Example 2: Comparing Linear Regression Options

Go to the PyShiny Playground. 
Run the [Plotly Example](https://shinylive.io/py/examples/#plotly).

For this example, we need three files:

- We'll replace the code in the app.py in the Playground with our **app.py** code.
- We'll edit the **reqirements.txt** file to add more packages.
- We'll add another file named **utils.py** that has some linear regression code.

### app.py

This Repo: Click on app.py above. Select all the code (CTRL A if Windows or CMD A if Mac). 
Copy the code to your clipboard (CTRL C if Windows, or CMD C if Mac). 

Browser: Click in the Playground app.py tab. Select all the code in the app.py playground example (CTRL A if Windows or CMD A if Mac). 
Paste the code from your clipboard (app.py as shown in this repo) into app.py in the Playground (CTRL V if Windows, or CMD V if Mac).
Verify the code copied correctly.

### requirements.txt

This Repo: Click on requirements.txt above. Select all the code. 
Copy the code to your clipboard.

Browser: Click in the Playground requirements.txt tab. Select all the requirements.txt code in the playground example. 
Paste the code from your clipboard (requirements.txt as shown in this repo) into requirements.txt in the Playground.
Verify the code copied correctly.

### utils.py

This Repo: Click on utils.py above. Select all the code.
Copy the code to your clipboard.

Browser: Click in the Playground code window. Add a new code file. Name the file exactly **utils.py**. Spelling and capitalization should be exact. 
Paste the code from your clipboard (utils.py as shown in this repo) into your new utils.py file in the Playground.
Verify the code copied correctly.

Click the run arrow (⏵) to see the updated app. 

## Links to the Apps Running in Shinylive

Example 1: Random Linear Regression

- [app](https://shinylive.io/py/app/#code=NobwRAdghgtgpmAXGKAHVA6VBPMAaMAYwHsIAXOcpMAYjvocaeYYB0IaACASRlWIBOZTgAUohANZQA5nADOnAGIBLAXLLsWW7Y3abR2MgAtSnAMpkoEACZQB1zgBllAIwF3so8VNlz2yvkFhdxtiGH9AoU51KDJldWVCPwgAMwEwzjJsVGUIaU4A-ijndTxOABUAV1QAGzg9DlEa4jIazxTBAvI4d0I4gDc4TkIjOzJkwqDOWpa2jDgAD1QBeQUoBVQFiKLhGdbsDGl3VCMAfWIXACs4PrWFaWJ2NIy9uaO0M4vLuQxTlOVpJUVgVIsIVICVg0uCJsGYjLlPKhvDJ5E90jBovCIAdFstViCdpxKspOJw0Rk5FjsAB3ZTWWTjAlTFY2HqnV7YKE6bksfQAETg-wgQwA4s0XFAapwAGp2ZRQFx1ZI8lW6CD6MxwYRyMJDXKoSrCfpyhVKsmNbgQQg1SrWIa2SyZbJDLHjdjSZSDCCnCCVGDs4i5caILrCAC8nAArAAGd2eyinOTNVBDEMpZqxTgRgBMGFjeXj3qDPUIcFQwjTGfDnAAjLn8x6vT7A3I4ImyA5K8RMxGa3muarVfzBbkhopKla4qRlYOh+rGgKhUMoJwUhO+spTGRiJxZML3BROCvW8JiClOAsyp4HSv+EHlRUjEMke54BQ1Jw7UvMk-OMaBPKipDNA8AKJUrYOM0hCSm0ZS5HIdJDMY8SruuU7zl+u6UD0sRtjeAb3gAFL6-p3uQcghkGZRJsQKZdrEcHdAIpblvRZBlBALZtuo1hsQAlJwAC0AB8FTVHUwAlGQwDpt2ZAALplFJMlVvJ8mIOwpKkgA5LpIrYQeQyXpw16xLegbkZwtLGEe0QpoQyj-HAkGjnYnArDUsSbhAlLKKgR42JwnHxHAGC6dpDRaZwXCasIxhDCE1gUnAzmrp0KzLMQ1iVA5LjKDUyhZJpWmJWEGCts5hHRnxxWkrV0WcPp+64bZBXqJwZ7uVYSUYgsf6SpU8icC4WrUilECcNGAUODW9ULKcbVkCGymybE8lZpwwClTAGDbYRAkdAInCnF0XV5HAxF+gR5F8fJ9X1VwTU4YeK6LR157Ba2-U2kN4G5PkK4ilA4EIVYn7xGQAEuIa3kPY+wFcQUCilkxqV2MQE4OFN1lGLZMQ2HYDh2v08roe9QVce21j1Z9bbGj9FFOBDKlyetEZbd1ZXSMDchyFVHGUzxB2dCduRnbIl2kRZ4y3fdE1aVwADCkqEJUnmHvFwyCCscj8DY-0md9g0KBKEEdRNmsFcKblwAAjpUXmmJ4EYwH1ADUw2cB7tP1dgC0Q8tzOrQpG3ADRKacAAVBeXuhiWZbCN7iOHReAshadABefmEfNi1p62pz08bsvy3VpcNQASlqQIW7+e7PalfXdYbRdDestlkOJSE7tSowUIMR3QTUNQKMhChrpOsPlysncCBNucQ1e-vqAOs7csO36azCcIIpwACiSw6woACq3CaGvPJQpwx9fVvsJUkSyhYCi5zlnzAlviYDjbtEWo-khhU6jmmJM-WQr9xiETiK0OAYZWBgGcNbI6VcjirG8k0FocCarzi4DfIYICjA1n2pwT+WVMg7msPEWoUBPDHhuKQawgk6iDClE+KAFC8icEIkYbMAl9BiF5qdY8kMDYUGHgbXuiRcYkIcGNIkEF2D4OzIROBAAhYkNRhA43MJYOICQkheEkCiTBV9cGPywEQ6RZDwa608jQ6YdgZDHFxoRVAWDoTrAUGLMGKRBLqAAhwwiK5DowFiBQBwfj-puKsSQGAeVhSZEWMIZuWiMZHX1IaI29RfRP1QIRFIcDFYY3IOTEQ0tGYgEbAmEi11xgAF9jHznPhfHQG9RycAAGScCrqyI6Ihmj7E4IrUYQgmnNK0A0dgAABFkdoBDsn6W0dgmE5DQTIO+eZLQiEiSUACIEcANLl3CpwRcbSgloTQcYTMM8a5rHQQM8EezwrFThsrYeHUgSoUnluHc9dDLvKOn1N6zdPBvU6q3ZIUUFh5xMm9CMvzcKnHwmRCBlTvTVORXIMoqLEzJjgFiwspxizMQTvipstMqZYKinDFQwgrZwDcisFBvM0EwCynAKUqL-kx2BZwRaEKtLhzxXHYl5YNoxF0XEJIGA6V2FOIyo+3kc7QuwItSlWkXkrBaiuYU1JpgLM8Cs0JPRhjDOEM8DEqTPxmXqv8fIEZNjlVWe+ZR5dIVhihYvc0UUorYDDCqz19UoqeRGiPMMIBtILG0iGbSAANbSZRtLYCjZwbSABNbStSyiBq0lAuoYZ8nwNckguATKEKmAFKyzhZhcUhhAIKxAGAADMKRM08CYixJanAQBEo7Q25ttSapgCwS8lWasWqa3lag0wdK5EGzejEvET4fJTyilwKus8Jquzdi4NKR16UjBjmLTWgKIb1Uncy0g-t4ns0FVHGOHse0J13Ye+ei07rzlXYMzVL09WzBBW0v6HCHV0qISQHykMcrbiOtIjAcNTGa1tY8tY1hrCnEhuIC6H8tRfzhvwzxtdgJwF1TO2RhBv2pR-mwhwhUrGaxGGMG1AIMBUbQ70C6wHRw53dcqsM56y3ejpXxDAN5gDRnksO8ua7q5z3-jsiEQwvg3Dij3PucAB7DBgqPeE49zmkDPdJiatqwCZvACBBAyAVj21UHAeA5EMBkAWGQfARBSAUCoMgJEBNkgcnYMZ+SQA)
- [editor](https://shinylive.io/py/editor/#code=NobwRAdghgtgpmAXGKAHVA6VBPMAaMAYwHsIAXOcpMAYjvocaeYYB0IaACASRlWIBOZTgAUohANZQA5nADOnAGIBLAXLLsWW7Y3abR2MgAtSnAMpkoEACZQB1zgBllAIwF3so8VNlz2yvkFhdxtiGH9AoU51KDJldWVCPwgAMwEwzjJsVGUIaU4A-ijndTxOABUAV1QAGzg9DlEa4jIazxTBAvI4d0I4gDc4TkIjOzJkwqDOWpa2jDgAD1QBeQUoBVQFiKLhGdbsDGl3VCMAfWIXACs4PrWFaWJ2NIy9uaO0M4vLuQxTlOVpJUVgVIsIVICVg0uCJsGYjLlPKhvDJ5E90jBovCIAdFstViCdpxKspOJw0Rk5FjsAB3ZTWWTjAlTFY2HqnV7YKE6bksfQAETg-wgQwA4s0XFAapwAGp2ZRQFx1ZI8lW6CD6MxwYRyMJDXKoSrCfpyhVKsmNbgQQg1SrWIa2SyZbJDLHjdjSZSDCCnCCVGDs4i5caILrCAC8nAArAAGd2eyinOTNVBDEMpZqxTgRgBMGFjeXj3qDPUIcFQwjTGfDnAAjLn8x6vT7A3I4ImyA5K8RMxGa3muarVfzBbkhopKla4qRlYOh+rGgKhUMoJwUhO+spTGRiJxZML3BROCvW8JiClOAsyp4HSv+EHlRUjEMke54BQ1Jw7UvMk-OMaBPKipDNA8AKJUrYOM0hCSm0ZS5HIdJDMY8SruuU7zl+u6UD0sRtjeAb3gAFL6-p3uQcghkGZRJsQKZdrEcHdAIpblvRZBlBALZtuo1hsQAlJwAC0AB8FTVHUwAlGQwDpt2ZAALplFJMlVvJ8mIOwpKkgA5LpIrYQeQyXpw16xLegbkZwtLGEe0QpoQyj-HAkGjnYnArDUsSbhAlLKKgR42JwnHxHAGC6dpDRaZwXCasIxhDCE1gUnAzmrp0KzLMQ1iVA5LjKDUyhZJpWmJWEGCts5hHRnxxWkrV0WcPp+64bZBXqJwZ7uVYSUYgsf6SpU8icC4WrUilECcNGAUODW9ULKcbVkCGymybE8lZpwwClTAGDbYRAkdAInCnF0XV5HAxF+gR5F8fJ9X1VwTU4YeK6LR157Ba2-U2kN4G5PkK4ilA4EIVYn7xGQAEuIa3kPY+wFcQUCilkxqV2MQE4OFN1lGLZMQ2HYDh2v08roe9QVce21j1Z9bbGj9FFOBDKlyetEZbd1ZXSMDchyFVHGUzxB2dCduRnbIl2kRZ4y3fdE1aVwADCkqEJUnmHvFwyCCscj8DY-0md9g0KBKEEdRNmsFcKblwAAjpUXmmJ4EYwH1ADUw2cB7tP1dgC0Q8tzOrQpG3ADRKacAAVBeXuhiWZbCN7iOHReAshadABefmEfNi1p62pz08bsvy3VpcNQASlqQIW7+e7PalfXdYbRdDestlkOJSE7tSowUIMR3QTUNQKMhChrpOsPlysncCBNucQ1e-vqAOs7csO36azCcIIpwACiSw6woACq3CaGvPJQpwx9fVvsJUkSyhYCi5zlnzAlviYDjbtEWo-khhU6jmmJM-WQr9xiETiK0OAYZWBgGcNbI6VcjirG8k0FocCarzi4DfIYICjA1n2pwT+WVMg7msPEWoUBPDHhuKQawgk6iDClE+KAFC8icEIkYbMAl9BiF5qdY8kMDYUGHgbXuiRcYkIcGNIkEF2D4OzIROBAAhYkNRhA43MJYOICQkheEkCiTBV9cGPywEQ6RZDwa608jQ6YdgZDHFxoRVAWDoTrAUGLMGKRBLqAAhwwiK5DowFiBQBwfj-puKsSQGAeVhSZEWMIZuWiMZHX1IaI29RfRP1QIRFIcDFYY3IOTEQ0tGYgEbAmEi11xgAF9jHznPhfHQG9RycAAGScCrqyI6Ihmj7E4IrUYQgmnNK0A0dgAABFkdoBDsn6W0dgmE5DQTIO+eZLQiEiSUACIEcANLl3CpwRcbSgloTQcYTMM8a5rHQQM8EezwrFThsrYeHUgSoUnluHc9dDLvKOn1N6zdPBvU6q3ZIUUFh5xMm9CMvzcKnHwmRCBlTvTVORXIMoqLEzJjgFiwspxizMQTvipstMqZYKinDFQwgrZwDcisFBvM0EwCynAKUqL-kx2BZwRaEKtLhzxXHYl5YNoxF0XEJIGA6V2FOIyo+3kc7QuwItSlWkXkrBaiuYU1JpgLM8Cs0JPRhjDOEM8DEqTPxmXqv8fIEZNjlVWe+ZR5dIVhihYvc0UUorYDDCqz19UoqeRGiPMMIBtILG0iGbSAANbSZRtLYCjZwbSABNbStSyiBq0lAuoYZ8nwNckguATKEKmAFKyzhZhcUhhAIKxAGAADMKRM08CYixJanAQBEo7Q25ttSapgCwS8lWasWqa3lag0wdK5EGzejEvET4fJTyilwKus8Jquzdi4NKR16UjBjmLTWgKIb1Uncy0g-t4ns0FVHGOHse0J13Ye+ei07rzlXYMzVL09WzBBW0v6HCHV0qISQHykMcrbiOtIjAcNTGa1tY8tY1hrCnEhuIC6H8tRfzhvwzxtdgJwF1TO2RhBv2pR-mwhwhUrGaxGGMG1AIMBUbQ70C6wHRw53dcqsM56y3ejpXxDAN5gDRnksO8ua7q5z3-jsiEQwvg3Dij3PucAB7DBgqPeE49zmkDPdJiatqwCZvACBBAyAVj21UHAeA5EMBkAWGQfARBSAUCoMgJEBNkgcnYMZ+SQA)

Example 2: Comparing Linear Regression Options

- [app](https://shinylive.io/py/app/#code=NobwRAdghgtgpmAXGKAHVA6VBPMAaMAYwHsIAXOcpMAYjvocaeYYB0IaACNTHdlgYMbt+QsS36cAkjFTEATmU4AFKIQDWUAOZwAzpwBiAS3m6yo8ZfoiOK7GQAWpTgGUyUCABMo8z5wAyRgBG8j7YKmqaOrrsRrIKSqFexDCx8YqcZlBkRmZGhDEQAGbyKZxk2KhGEFqccXIZgWZ4nAAqAK6oADZwLQDCUF1dUEE9NlwAogAeFPLQXREa2nqcABQw7WacQXB1EFlDcJ4AlJIAqrq78nAAju0mcPDkuhhkM5JNSqS7qJHLnKg4PJOF1qnBxiousQyF1wkUFHtZmocgA3XaEBw+MiFeoJAFQmHYDBwKaoa66fRQfSoKZpBpKbrQ2EYLShVAOAD6xCCACs4IRsdx9FpiOwSmVGYSWWzOdyeS8OUUjFp2tc6uklMYVdcIcpsC4HNVwr8ltExaUYJlDRBwriMtcvECWtdkUY0eayrprUSSWS9Po7Up7i1qqh2uZiharUaAO5GTw6QWBzgOzxAjmS2EQ-zEQiDTgwYiedo9dX0ySgraDBaOXZkYioAC0PTRCxRPiMIx6lK8nCK7QgAqMpH0Md2EDgRz23HQWGwHst4aMXQDGs4U0rZBa2E3LQ3uTIACZt5vj32B0PSBzd+fBzkrzAeNUtC007pCPIjKh7xAOY-0M+LSJhyuhQoCHIeJ4HLVLMhBwN+4xWEhkgACJwEqE6cAA4lCQT5gAah2XZ6BYSHiBCfQuhQnCePkP5hH2CKeKUqCeMQMYQJwDY-oU-Z3sOv7cQJugcrRAqcAAvJwIDsJwcmcKwYBZOYSAKWAbh+IEQSuO4OR5AUil4LJ8mKRA7SyPOqmKQAcuZeqGcZcmKe+X6WYgakuIQRj2fgjlqcpuiFmmK6Ke5iluNkgVFnAIW+ZxJlKeoPQ+BAoUeV56hGGQjb+HAKUOfFTlgA47Q7PIaXhRlWU5XlcycAAEqVQIFfJalJLoagVepVXZblKWcAASgAgtZLhDX0BUAL6IWR5G2GhGF1g4ux6gaRqcNMfoUpwZxSKRs2CBCFxLSt+repw9xYMsXLfroqzHAWcCOEW5TEJkT3lMt5RZaW7CXb8Og3diqw5DCcASYpADqDjhChb2Q7sLh3D4uwDXo8btIMAacYEE4+INcCsv6AkAPyKacqUQHGjgXUYGC6PGcB4fIqxBFoEO0BMEwGIeBgABzk+5CmFWpx3Ai4MX8jxinC35l2huGIGSwKqx+a1znKxQUFKqYZB-k9TieC1rUJQAsgbL0AIzGybt6XoJ37CaJdFGSLrWXD0ApHBzymKX5FNy3TCt6x7Uuq27CWh17UGXCQXj689RtxbbRXm4nnCHogNsm3x9tA07Ylbmr7ua97iklWVfsiwHIvyxAYYh5r4cp-5pdQd47iXCprst4pfROMQlzcDR2RUk9WfJynMlgNbSCKSho9d5ws89ynimHqF8+Lx9G9gJNq8p1HWsc7P-s2PtB0SLYaOuminB5l0BTC1wZysdkuxQOGKTZPk1bhDGy1OLB30BiDwOgL6XyYBCG+Q474P0ICWH+I5GLAiPlOXO0sIAAAEXSwLgBgeB7A0xFHep7LWioLw-g5Jbe6WcRbXDIKqTiGCBJ-ifDUYAwd6Zt0VCYMwCdDb3QALo2BwXlPBBDBiECIehUhUsjgUP4leQ8tC-IMKYXbKh-4qgcK4WgmO-JSBQXgInYRojcGonwYQx0JDEwAA0ACaqiRZGBIXonhHcx5kHupJKSilZ50Jbuouq+5micB3AePyMVLiBJTsEzioSjwngPBvSmkChCoXQmCTgAAyAmjpgQAHlwwNwgek6wlNqYOFphgYY2BiCKxIF0cy+xVhNI5HGTwjhdASVWAANjwH044xxYlORFlUmpeZfDON7hHOSYiCmvBJBGFuxDHqJxoSM4utt4l9kUiAFhV4hIjmdgKTh9dwzcLIQonW-CTGCOOEI6aYAbAtwWWmeQSz3hzJorIt8H4vybNGS3FMT0NFFH2f8z8jsHzsK0OchuVz5Haz4Xre5RZhHPNktszg7z0yZnnD8tZ75sizAzASTZnBGwAD5DDKlVHAYFLcADkrLOALWyVATRAlPrZFBYwuYlJIRMnCFqBlrLmWvJBXJdFfgpLuOuSi3WAiMUU2lXJKY7Zml6G3Fq9oKwpL2KcWq9VoEGy9ERECOC35JKcGAma8CkFoLkCtfBbxmrBj6t0Lqz1Or1mGxNdKnFrUuCUTytRLlE4Yz4hFZkPMZBZj30xBkcUloGnAk8cG+SSpahSRpPTeNsxm7qtalMCSHrtXeuFiW1q2AJLYD1X6rNtthg7BXBJEAzKpjMvcsyuxzKWjMuwD2zgzKHHMv3tWmtclQY9AkhC9SYFGXSQdYyjAABmIok6pAuvkNasg7kQAwVdd+RAG6t3k22c2zgoapGIOorWUFRMKQ8tBJhTYz4QQHnvikP0gCGakGvVwNGArOIwCmAAam0vCYE4jqlTGnI+hDm5r3XGfQB38b7dhSWAKuzgAAqdcnAIOWr3W6lBRHqjrkbboERPygOcDDe-YeBKv3voZjUAEUxalgh8XHMw8h2gCgRLKjADHjqfV2Dm8VlJPBQTIKEOCPjZUMdUNtKjj6o1sd2GOe+VEpz1m4HJuoShDOPtAYoa9OaMBQDkxyBTag4CrHzVh1YZaK1eu3BJND5IMPXjBMcDAnjgAAAYhGBpNgxkDGjH1irVHKKWr1OAAPfmiYED8VyfVyNywDPzWq7JzY5KVckJmXSmZ4GZa8fl4s+RQb5qzZGypUVsvL8kCv7MOQ7HipyyAIsufopWcdjEWwq48rFlM3mpiBF8lZKc1lQq-M1plcSwV1QXSABbMLfzaOfH1sgSLo6DaMSq0bTyq6zMm5QD55KRU4uJYW-FBJ10+JpXS7UjLr0SvZVkzCXLOu8sSKt-Yw9lAElhG98VrKcXXtlbahVyKjvx1lfda9Hm-UNt9foQ1T1HEo9a3JVdIZd37ttfapdEF47HrI9+NzNGfWVpaLKiLF31U5ttfmklCagTFune5unU7p11oxwzgXNbW3RI7V2kdfaB2juHb28dk7r2tVneDBdLgl2HtXWezd27idusPVT-dOuL1gGZyZfHT7fOsKw7a3DS6CNEZI0b8jMHKMJJo3Rkt1nbPycU05lzvG+eY68z54mV4sOBeC2F83Oygd9mVI5PeeBwDQHgNQa4dwHhPGxK8GY+AiCkAoFQZAvwvBUnYAS9gZkLLsBcnwfYukorBUKC5TK2VkpzGT6n2ACBkBLhXHOAvcdi9kGoOUgQkgB-6CCiWXYjYyx4hgm9Hgc4ykT5mhP4QtgZD0kWFEFYxhdbr-KbqewThOIRXL74AIwRQjyHCKoU0JEIDJgKCiOkeJlIHnyLxKMFQdFahkxPgWgOhuhwQ0kNoZggR5h99lh9B1hNglAdg9gDgegThzgh5M97hrgc8Xg3glBIIv0thJBClMITQD8AQgRtMbBkwa8cAhROB64Fw41XJF8MgApP8OCm8gpokbMqhGDAoWDdAkpaoIAeM8Z5A-xooFhgCwQfA0Z0MBIWhGoypFDfMFAWhhpRpxp1D-QFBN8t8KkuAOVMIXBYBwD2VR5XAnpCgjCoFICF53AbClBrZbBWgYw3pNx9BiASEigoQf5OM5AYImDzIyoq1vgKMEMiDIi3dCVEl3JPhgB-DiBsghE7dLYMAQsWhDwsiWh108jOAAAWQogAVkKL6UKIAHZCi+Ysi6MIkzBEiDxkiAiyB0icNcjLZ8iMAzxKjSiWg6j10WgABODAIoloS2XIvmSYgoqoyYyoooujVCawiWJQVJLgDwrwg8Hwvwtoz9YI8gUImAcIloWIhEaI3sc44EeI08ZoswVo1I9ojIwo3I7IzgAo94ko948o94yo94mo94uosLdgRoo8e43rFItIu3LonovojAAYzgIY0Y8YyY6Y2YjAeY5eELELeo2WNJewtgeaH7KTShG3SJDgQkipGREheg7AfzSQjkMPF9UgVYOxCEx4tI7cDkqE9oh6V7MAnoTkrcPsNooRYFL7CTWyGAPUW-SQgmJQ5wVYfwU2FwY4CVPyOxW1euGzeQUIbANkiLcIKSHUnwfU1YbACLLUk0zAFELIDQVYYAHU74O6HoCAQ044FoOxcLDAVoOSLgIaOTbGWCcjWYVIEWWsZwm0iQwYLQDAaoFENk303FTgOxB6LBVM5MjMwlfLePSMqAYAS2IRFofM0LdIm9AmUDfQQnUjfdGwe7VyBk2qJkwma3Vk9k2-B43k4s8JHksU-k2lQUuAYUlobsiUtlCTTybycIXGWqBUtsziZU1U9UqHEWGsl3b8FoDkLcrc21AKCQ5ku6OxbcCLXZdc-XBCSmYlHgmQkSLDHwFsxU90jspI7s7kzsyE-sqlQczoIU3k0csU8c5lHaIeCKbEXgzLWc-GPQlkxclUtUjUkWa0zIGAGzOzfjdwcgQ0-0zgQMzwYMk9UzIEcM1qCCvc1CwpfwFwC0r0wLJUbxCLc8kMm1KSCCq6UIGAXQQsnsti34DirikE+hePJiwi+s2REQzvTDeQqQw8gSNkvsp4ns7ABStIgctoX84c-80UxSoCkCxGHqGqfqKC4EGCjDNYeClcyVEWMiqSYy0yuSiLNi+i1YU0vUqAA0tMjAckTEQEVYRsbo5eT08JU8+PNikgdCDkMsxnGQ+Mi8vWMSkhCSsQjkCudMWS9slS9o9818r8gUjSkc7StI3SycgyvqOqVQ6g+ypU-wIaFCSyvyGyhqJqeQUyhQe6DAZy1y80zy7ytAJzfyyYoKy0tRUKmK8KooSKsLaK4KWK5i+Kq88S0QlKJkjwDqQgR8hc+Sj84UpSzK8Lb89S8AgqscvySU0C0qsQwaEaMaPoec8POC5cxC0imQ21bQm61qlmOirKFyzAM09yw0ryvQHy-qgKy2IakK0DAsGKvQHIR8esKQghYgCKqKqGmamGuIbIBQDkWawijkBKmiXIbody+zYiVYckEsbEDkwuHstMLyR8LoDMYgGCXQdyGCV8beA9TIBTNS6yb4IClCQmupUFXQCm7GYeGDOGrWcoYiCjLlXQQELyJUQgEeTuJ6J6+SMkGCVYBdVgdgNGEWroQUN3DbDmyaFWrxCeCLTWrC-ZRAAAHkPFKLNpAHtsthC2dtdsPA9rtqmOeQ6oUDhtVjADTkNkMjUlaEqHBHwA8iXTDsUh3TmvJits-BtrAA5nwz6RCwiwluyBAgU1tXWxdodqdudqLrdsmlLs9owA235AxoZsOOxEmi3Urp9tyJrrpsGEZuZqborvO2zQRHJsNunEHsppxVcWFopuAC3lVpUg6Kkk8S7mW1tmtu8RzpDgU39vkEDpHqnuDpG0Uh7J3sUgjsBAPudD0EnvCljrAEPovsNt3oTtEpvuGXxq9HYhAhgBAnMkfAfy2pysUuypaO7J5r5tOtZQFvlqFrTHcGXCnBFpgB-rhARDAub2iTlLnKqogHVrkjsQ6Syk5AwvIrQqggwo8G8TTL8kCmkOCiIcououwC9LwccA5Awq+oYr8hXtWCobYvgcQfuhripOMO+0Wlwo-K4hIVaBhsOu7BP3SWzG-V8Jy32BaDg2HkYUsImWqDXoEhsE638y2Bwz8iDo0lv20jAp-wMmju-30heHvJktbPupaEUngvJgPjWBsjskshaDpKbIfPSogCcbABcbNzceMa8h8haHr3pLsY2scbUmCc9KMfChvJbzDoCggrvOktidgsCYSdCcqiMHb0MrmDSaWrmF8fsafNydVNcaSe6kKeqjKs4gqvKisbKd-FSsqYXMCYGm5CQNqZFjCYad6kurevGlKckpWv2DUGyYwx6b6bMEvQgGWPmjogEgYlWHUDgGwEbEbQBCgD4QekUc6zsM4FNjQGHjfu4JTtqDMy+mRExgWH+zTwgLFDJNhQAk4ykhkhFmcl0jSmsZyAKAkObP8bcdMnMj4FUh8ZibBb8mci8ihfciiYqdmeUPhaUhSeiQBaxZXFRbhd+cSkkoBfafxYcZyYxc6ZJcmc6bRdIHBbAHak6lUiSuWqZfWv8fYGmgWvfGhS0ThVtR+fVkxeyC6j9nUkwu8Bvy0nv3CEBd-xBb8fJYwx8U2BWGSi2F0GRnJCt3uvMuXLExeSNYZbpLFaNelNlLVf0A1aUC1cxh1f8f1bVO2HCFomuAFHBxIFkCXE40fQTKBCHkUcfThs-G43FezgRdcjNYKb1GZWrKbwPOVYukuGtbyk1e1ZWEdaXLVMNfFYZfSdvOjYlcigyeTZWDobWEKV8GqAYj6i2CRntb0Aelh0M0BHkAluHhtcyAzf0CzYstzeNYxdZZKasiNYKaKaafQYUOVZ5StZBDTdtZ7d1dgqdcC3DcniKipdHfFanInbELjaarUOVYRDndKCCCQOXbMomS5S9aCBrZ-HEe7cbb8ChG2jd2qFBADe4F7BGF0GIGaWolff0DdwaRhCMADcZygEyk4yynne2kuH2CyjdDrDelA8-dMF5RxlVIHYjcZdWuZbCjHfqb3ZSgPbGb6A+rLd7YWcByfOS3wdwqCD-YA92DQhRE7B-BDCREsXB3ov0GDZkJaCINwOIDRB8PDHQ6rUfGg6AIZCxHyEQXkHB3QiKClmQ4owXtsPo5pkfBtC4gk-A9MBw5eQgG5ZpLtSehAnJydQ3PIb2sAa7LFMZxG2Re5oOqHOOsArAeAuUFKHY7TEufqFLH+0cD5TjCGCoPbYDskyTUHkoH9RelWDloU2fEC2wYLGyAxAS88CXvvjHn8n+bnktzPN0gsdsayf8bZJPJxTzCHghdryK5LV2RhYq5nfbOq5+Vq92EjaRdQ2EsReida6fKq+Cpq-y7+ZLcLca-VRK8m5bzJeG+PNG86-G6JbEM3mK+EtJdhba+fI65bi67Ui3dy9zMhuHY6earpb2+W4O9W-ZY26a628mfZau5G+GpW6Hg5BO7awOaHkIm1QmD1LaoXTOAgHUAgHYjAxc+kllWeRrjWWAk2x-HWGh4EzUoE10qwg+iR55Tdy0GQ6h8TgwHS7hqy9lVy8O4m5Um+7kl2UUlptabG7q8gEhbcj68hrUgZ77ttkp6UgG4e5m-j05-5EZ4++65FfAqm5p-5Q0WF4-G55Nl5-O4F+lTp7AC55M9u+Z+O-Z9l-p5F4V9al5-u+m9V6F-1-l815TkO6+9Q1+92H+-1UB9KBZhB7B4h44my8PVh6WfPkpMEckD6CMSQ9IHzGmH5CXGcFkcgVoJIQ5A5Befj98TUnj8fGqHj4278kEboCz+kBIV00E04kcGy1n1LCpEuYBU3MkyL6kfTSUcKBDTOag92BFrVFrCHhOeSwUHUB-T1KlizBFi4B2Bg12EDE-Xb9JKUWB2X2-ehGWmBFL-wSz+z+KwrP1tFuINMzejMAUF2FUZHsYK5ULnWYfxGoNsFBwxWcb4GgHE4FUf+yIJ37VBHuA4RCcK5TWOXj8jdxedHIvGc-ThUY9Gm4XLiJWpxKApIucNzDeDBKx4J6htF4DwCuyrBp4IdIsGlF-7h1I6aUWVIEw1zmoAWS6QJo-XAFpRbOgTd-l3C6izxJoNca-rf3v7vNOIj-eGlcDvpG03+qxHeN-wRCYDc4AAw2NOGAEHhQBRA2suRkgEXhoBKSZJGYEPBwCX+-BQEF4BQGKQ0BScdyJgOPrYDVIuAmOgQJZZiD46cVMgXFQoEc0uou8Wgavy4CQxPw1EF-klj6AuB8ICeMYOMgY7mp3SikHbk+RbLn8Xg7+OOmABjBh0o0WGDmOTEYLv4lQPQXLkqBiieAXmWOTgLvXUHBCT6UdPAdfWIEmDo609LxAfRxQxh7B1BKSO-gwAC0BQdgrKNzhiGwNRy4HLoEkN7w9IEhzQ5IXQJTglDahnyHoRQGWi2ZuccA-odNlGGlAYwd0F-l0JwoQMia4QR9I4PL5cp3AowHTAxz5i-IO6CwBuq-1QQO4iCtnPyLREgbE1VhPQMmuwKrQzE1Is8CLCcPmEk01hlwgIYMUCa7wZhFZPCiH1gLQMDm6BTIN-QYipodIc3NBhwxTreI-Y7ANCDAwBEuAgRD+CjCg1LbGU7qK7VYJQI+hg1LalDJwDGA-pf0EGYQaQWElgGr9OG0IiALCP+FTgERxIpEW7hRG3kp2JlXbmsCxHrEtkZuPEe-Soa8MSRiSM8GCXkF7whEQAA)
- [editor](https://shinylive.io/py/editor/#code=NobwRAdghgtgpmAXGKAHVA6VBPMAaMAYwHsIAXOcpMAYjvocaeYYB0IaACNTHdlgYMbt+QsS36cAkjFTEATmU4AFKIQDWUAOZwAzpwBiAS3m6yo8ZfoiOK7GQAWpTgGUyUCABMo8z5wAyRgBG8j7YKmqaOrrsRrIKSqFexDCx8YqcZlBkRmZGhDEQAGbyKZxk2KhGEFqccXIZgWZ4nAAqAK6oADZwLQDCUF1dUEE9NlwAogAeFPLQXREa2nqcABQw7WacQXB1EFlDcJ4AlJIAqrq78nAAju0mcPDkuhhkM5JNSqS7qJHLnKg4PJOF1qnBxiousQyF1wkUFHtZmocgA3XaEBw+MiFeoJAFQmHYDBwKaoa66fRQfSoKZpBpKbrQ2EYLShVAOAD6xCCACs4IRsdx9FpiOwSmVGYSWWzOdyeS8OUUjFp2tc6uklMYVdcIcpsC4HNVwr8ltExaUYJlDRBwriMtcvECWtdkUY0eayrprUSSWS9Po7Up7i1qqh2uZiharUaAO5GTw6QWBzgOzxAjmS2EQ-zEQiDTgwYiedo9dX0ySgraDBaOXZkYioAC0PTRCxRPiMIx6lK8nCK7QgAqMpH0Md2EDgRz23HQWGwHst4aMXQDGs4U0rZBa2E3LQ3uTIACZt5vj32B0PSBzd+fBzkrzAeNUtC007pCPIjKh7xAOY-0M+LSJhyuhQoCHIeJ4HLVLMhBwN+4xWEhkgACJwEqE6cAA4lCQT5gAah2XZ6BYSHiBCfQuhQnCePkP5hH2CKeKUqCeMQMYQJwDY-oU-Z3sOv7cQJugcrRAqcAAvJwIDsJwcmcKwYBZOYSAKWAbh+IEQSuO4OR5AUil4LJ8mKRA7SyPOqmKQAcuZeqGcZcmKe+X6WYgakuIQRj2fgjlqcpuiFmmK6Ke5iluNkgVFnAIW+ZxJlKeoPQ+BAoUeV56hGGQjb+HAKUOfFTlgA47Q7PIaXhRlWU5XlcycAAEqVQIFfJalJLoagVepVXZblKWcAASgAgtZLhDX0BUAL6IWR5G2GhGF1g4ux6gaRqcNMfoUpwZxSKRs2CBCFxLSt+repw9xYMsXLfroqzHAWcCOEW5TEJkT3lMt5RZaW7CXb8Og3diqw5DCcASYpADqDjhChb2Q7sLh3D4uwDXo8btIMAacYEE4+INcCsv6AkAPyKacqUQHGjgXUYGC6PGcB4fIqxBFoEO0BMEwGIeBgABzk+5CmFWpx3Ai4MX8jxinC35l2huGIGSwKqx+a1znKxQUFKqYZB-k9TieC1rUJQAsgbL0AIzGybt6XoJ37CaJdFGSLrWXD0ApHBzymKX5FNy3TCt6x7Uuq27CWh17UGXCQXj689RtxbbRXm4nnCHogNsm3x9tA07Ylbmr7ua97iklWVfsiwHIvyxAYYh5r4cp-5pdQd47iXCprst4pfROMQlzcDR2RUk9WfJynMlgNbSCKSho9d5ws89ynimHqF8+Lx9G9gJNq8p1HWsc7P-s2PtB0SLYaOuminB5l0BTC1wZysdkuxQOGKTZPk1bhDGy1OLB30BiDwOgL6XyYBCG+Q474P0ICWH+I5GLAiPlOXO0sIAAAEXSwLgBgeB7A0xFHep7LWioLw-g5Jbe6WcRbXDIKqTiGCBJ-ifDUYAwd6Zt0VCYMwCdDb3QALo2BwXlPBBDBiECIehUhUsjgUP4leQ8tC-IMKYXbKh-4qgcK4WgmO-JSBQXgInYRojcGonwYQx0JDEwAA0ACaqiRZGBIXonhHcx5kHupJKSilZ50Jbuouq+5micB3AePyMVLiBJTsEzioSjwngPBvSmkChCoXQmCTgAAyAmjpgQAHlwwNwgek6wlNqYOFphgYY2BiCKxIF0cy+xVhNI5HGTwjhdASVWAANjwH044xxYlORFlUmpeZfDON7hHOSYiCmvBJBGFuxDHqJxoSM4utt4l9kUiAFhV4hIjmdgKTh9dwzcLIQonW-CTGCOOEI6aYAbAtwWWmeQSz3hzJorIt8H4vybNGS3FMT0NFFH2f8z8jsHzsK0OchuVz5Haz4Xre5RZhHPNktszg7z0yZnnD8tZ75sizAzASTZnBGwAD5DDKlVHAYFLcADkrLOALWyVATRAlPrZFBYwuYlJIRMnCFqBlrLmWvJBXJdFfgpLuOuSi3WAiMUU2lXJKY7Zml6G3Fq9oKwpL2KcWq9VoEGy9ERECOC35JKcGAma8CkFoLkCtfBbxmrBj6t0Lqz1Or1mGxNdKnFrUuCUTytRLlE4Yz4hFZkPMZBZj30xBkcUloGnAk8cG+SSpahSRpPTeNsxm7qtalMCSHrtXeuFiW1q2AJLYD1X6rNtthg7BXBJEAzKpjMvcsyuxzKWjMuwD2zgzKHHMv3tWmtclQY9AkhC9SYFGXSQdYyjAABmIok6pAuvkNasg7kQAwVdd+RAG6t3k22c2zgoapGIOorWUFRMKQ8tBJhTYz4QQHnvikP0gCGakGvVwNGArOIwCmAAam0vCYE4jqlTGnI+hDm5r3XGfQB38b7dhSWAKuzgAAqdcnAIOWr3W6lBRHqjrkbboERPygOcDDe-YeBKv3voZjUAEUxalgh8XHMw8h2gCgRLKjADHjqfV2Dm8VlJPBQTIKEOCPjZUMdUNtKjj6o1sd2GOe+VEpz1m4HJuoShDOPtAYoa9OaMBQDkxyBTag4CrHzVh1YZaK1eu3BJND5IMPXjBMcDAnjgAAAYhGBpNgxkDGjH1irVHKKWr1OAAPfmiYED8VyfVyNywDPzWq7JzY5KVckJmXSmZ4GZa8fl4s+RQb5qzZGypUVsvL8kCv7MOQ7HipyyAIsufopWcdjEWwq48rFlM3mpiBF8lZKc1lQq-M1plcSwV1QXSABbMLfzaOfH1sgSLo6DaMSq0bTyq6zMm5QD55KRU4uJYW-FBJ10+JpXS7UjLr0SvZVkzCXLOu8sSKt-Yw9lAElhG98VrKcXXtlbahVyKjvx1lfda9Hm-UNt9foQ1T1HEo9a3JVdIZd37ttfapdEF47HrI9+NzNGfWVpaLKiLF31U5ttfmklCagTFune5unU7p11oxwzgXNbW3RI7V2kdfaB2juHb28dk7r2tVneDBdLgl2HtXWezd27idusPVT-dOuL1gGZyZfHT7fOsKw7a3DS6CNEZI0b8jMHKMJJo3Rkt1nbPycU05lzvG+eY68z54mV4sOBeC2F83Oygd9mVI5PeeBwDQHgNQa4dwHhPGxK8GY+AiCkAoFQZAvwvBUnYAS9gZkLLsBcnwfYukorBUKC5TK2VkpzGT6n2ACBkBLhXHOAvcdi9kGoOUgQkgB-6CCiWXYjYyx4hgm9Hgc4ykT5mhP4QtgZD0kWFEFYxhdbr-KbqewThOIRXL74AIwRQjyHCKoU0JEIDJgKCiOkeJlIHnyLxKMFQdFahkxPgWgOhuhwQ0kNoZggR5h99lh9B1hNglAdg9gDgegThzgh5M97hrgc8Xg3glBIIv0thJBClMITQD8AQgRtMbBkwa8cAhROB64Fw41XJF8MgApP8OCm8gpokbMqhGDAoWDdAkpaoIAeM8Z5A-xooFhgCwQfA0Z0MBIWhGoypFDfMFAWhhpRpxp1D-QFBN8t8KkuAOVMIXBYBwD2VR5XAnpCgjCoFICF53AbClBrZbBWgYw3pNx9BiASEigoQf5OM5AYImDzIyoq1vgKMEMiDIi3dCVEl3JPhgB-DiBsghE7dLYMAQsWhDwsiWh108jOAAAWQogAVkKL6UKIAHZCi+Ysi6MIkzBEiDxkiAiyB0icNcjLZ8iMAzxKjSiWg6j10WgABODAIoloS2XIvmSYgoqoyYyoooujVCawiWJQVJLgDwrwg8Hwvwtoz9YI8gUImAcIloWIhEaI3sc44EeI08ZoswVo1I9ojIwo3I7IzgAo94ko948o94yo94mo94uosLdgRoo8e43rFItIu3LonovojAAYzgIY0Y8YyY6Y2YjAeY5eELELeo2WNJewtgeaH7KTShG3SJDgQkipGREheg7AfzSQjkMPF9UgVYOxCEx4tI7cDkqE9oh6V7MAnoTkrcPsNooRYFL7CTWyGAPUW-SQgmJQ5wVYfwU2FwY4CVPyOxW1euGzeQUIbANkiLcIKSHUnwfU1YbACLLUk0zAFELIDQVYYAHU74O6HoCAQ044FoOxcLDAVoOSLgIaOTbGWCcjWYVIEWWsZwm0iQwYLQDAaoFENk303FTgOxB6LBVM5MjMwlfLePSMqAYAS2IRFofM0LdIm9AmUDfQQnUjfdGwe7VyBk2qJkwma3Vk9k2-B43k4s8JHksU-k2lQUuAYUlobsiUtlCTTybycIXGWqBUtsziZU1U9UqHEWGsl3b8FoDkLcrc21AKCQ5ku6OxbcCLXZdc-XBCSmYlHgmQkSLDHwFsxU90jspI7s7kzsyE-sqlQczoIU3k0csU8c5lHaIeCKbEXgzLWc-GPQlkxclUtUjUkWa0zIGAGzOzfjdwcgQ0-0zgQMzwYMk9UzIEcM1qCCvc1CwpfwFwC0r0wLJUbxCLc8kMm1KSCCq6UIGAXQQsnsti34DirikE+hePJiwi+s2REQzvTDeQqQw8gSNkvsp4ns7ABStIgctoX84c-80UxSoCkCxGHqGqfqKC4EGCjDNYeClcyVEWMiqSYy0yuSiLNi+i1YU0vUqAA0tMjAckTEQEVYRsbo5eT08JU8+PNikgdCDkMsxnGQ+Mi8vWMSkhCSsQjkCudMWS9slS9o9818r8gUjSkc7StI3SycgyvqOqVQ6g+ypU-wIaFCSyvyGyhqJqeQUyhQe6DAZy1y80zy7ytAJzfyyYoKy0tRUKmK8KooSKsLaK4KWK5i+Kq88S0QlKJkjwDqQgR8hc+Sj84UpSzK8Lb89S8AgqscvySU0C0qsQwaEaMaPoec8POC5cxC0imQ21bQm61qlmOirKFyzAM09yw0ryvQHy-qgKy2IakK0DAsGKvQHIR8esKQghYgCKqKqGmamGuIbIBQDkWawijkBKmiXIbody+zYiVYckEsbEDkwuHstMLyR8LoDMYgGCXQdyGCV8beA9TIBTNS6yb4IClCQmupUFXQCm7GYeGDOGrWcoYiCjLlXQQELyJUQgEeTuJ6J6+SMkGCVYBdVgdgNGEWroQUN3DbDmyaFWrxCeCLTWrC-ZRAAAHkPFKLNpAHtsthC2dtdsPA9rtqmOeQ6oUDhtVjADTkNkMjUlaEqHBHwA8iXTDsUh3TmvJits-BtrAA5nwz6RCwiwluyBAgU1tXWxdodqdudqLrdsmlLs9owA235AxoZsOOxEmi3Urp9tyJrrpsGEZuZqborvO2zQRHJsNunEHsppxVcWFopuAC3lVpUg6Kkk8S7mW1tmtu8RzpDgU39vkEDpHqnuDpG0Uh7J3sUgjsBAPudD0EnvCljrAEPovsNt3oTtEpvuGXxq9HYhAhgBAnMkfAfy2pysUuypaO7J5r5tOtZQFvlqFrTHcGXCnBFpgB-rhARDAub2iTlLnKqogHVrkjsQ6Syk5AwvIrQqggwo8G8TTL8kCmkOCiIcououwC9LwccA5Awq+oYr8hXtWCobYvgcQfuhripOMO+0Wlwo-K4hIVaBhsOu7BP3SWzG-V8Jy32BaDg2HkYUsImWqDXoEhsE638y2Bwz8iDo0lv20jAp-wMmju-30heHvJktbPupaEUngvJgPjWBsjskshaDpKbIfPSogCcbABcbNzceMa8h8haHr3pLsY2scbUmCc9KMfChvJbzDoCggrvOktidgsCYSdCcqiMHb0MrmDSaWrmF8fsafNydVNcaSe6kKeqjKs4gqvKisbKd-FSsqYXMCYGm5CQNqZFjCYad6kurevGlKckpWv2DUGyYwx6b6bMEvQgGWPmjogEgYlWHUDgGwEbEbQBCgD4QekUc6zsM4FNjQGHjfu4JTtqDMy+mRExgWH+zTwgLFDJNhQAk4ykhkhFmcl0jSmsZyAKAkObP8bcdMnMj4FUh8ZibBb8mci8ihfciiYqdmeUPhaUhSeiQBaxZXFRbhd+cSkkoBfafxYcZyYxc6ZJcmc6bRdIHBbAHak6lUiSuWqZfWv8fYGmgWvfGhS0ThVtR+fVkxeyC6j9nUkwu8Bvy0nv3CEBd-xBb8fJYwx8U2BWGSi2F0GRnJCt3uvMuXLExeSNYZbpLFaNelNlLVf0A1aUC1cxh1f8f1bVO2HCFomuAFHBxIFkCXE40fQTKBCHkUcfThs-G43FezgRdcjNYKb1GZWrKbwPOVYukuGtbyk1e1ZWEdaXLVMNfFYZfSdvOjYlcigyeTZWDobWEKV8GqAYj6i2CRntb0Aelh0M0BHkAluHhtcyAzf0CzYstzeNYxdZZKasiNYKaKaafQYUOVZ5StZBDTdtZ7d1dgqdcC3DcniKipdHfFanInbELjaarUOVYRDndKCCCQOXbMomS5S9aCBrZ-HEe7cbb8ChG2jd2qFBADe4F7BGF0GIGaWolff0DdwaRhCMADcZygEyk4yynne2kuH2CyjdDrDelA8-dMF5RxlVIHYjcZdWuZbCjHfqb3ZSgPbGb6A+rLd7YWcByfOS3wdwqCD-YA92DQhRE7B-BDCREsXB3ov0GDZkJaCINwOIDRB8PDHQ6rUfGg6AIZCxHyEQXkHB3QiKClmQ4owXtsPo5pkfBtC4gk-A9MBw5eQgG5ZpLtSehAnJydQ3PIb2sAa7LFMZxG2Re5oOqHOOsArAeAuUFKHY7TEufqFLH+0cD5TjCGCoPbYDskyTUHkoH9RelWDloU2fEC2wYLGyAxAS88CXvvjHn8n+bnktzPN0gsdsayf8bZJPJxTzCHghdryK5LV2RhYq5nfbOq5+Vq92EjaRdQ2EsReida6fKq+Cpq-y7+ZLcLca-VRK8m5bzJeG+PNG86-G6JbEM3mK+EtJdhba+fI65bi67Ui3dy9zMhuHY6earpb2+W4O9W-ZY26a628mfZau5G+GpW6Hg5BO7awOaHkIm1QmD1LaoXTOAgHUAgHYjAxc+kllWeRrjWWAk2x-HWGh4EzUoE10qwg+iR55Tdy0GQ6h8TgwHS7hqy9lVy8O4m5Um+7kl2UUlptabG7q8gEhbcj68hrUgZ77ttkp6UgG4e5m-j05-5EZ4++65FfAqm5p-5Q0WF4-G55Nl5-O4F+lTp7AC55M9u+Z+O-Z9l-p5F4V9al5-u+m9V6F-1-l815TkO6+9Q1+92H+-1UB9KBZhB7B4h44my8PVh6WfPkpMEckD6CMSQ9IHzGmH5CXGcFkcgVoJIQ5A5Befj98TUnj8fGqHj4278kEboCz+kBIV00E04kcGy1n1LCpEuYBU3MkyL6kfTSUcKBDTOag92BFrVFrCHhOeSwUHUB-T1KlizBFi4B2Bg12EDE-Xb9JKUWB2X2-ehGWmBFL-wSz+z+KwrP1tFuINMzejMAUF2FUZHsYK5ULnWYfxGoNsFBwxWcb4GgHE4FUf+yIJ37VBHuA4RCcK5TWOXj8jdxedHIvGc-ThUY9Gm4XLiJWpxKApIucNzDeDBKx4J6htF4DwCuyrBp4IdIsGlF-7h1I6aUWVIEw1zmoAWS6QJo-XAFpRbOgTd-l3C6izxJoNca-rf3v7vNOIj-eGlcDvpG03+qxHeN-wRCYDc4AAw2NOGAEHhQBRA2suRkgEXhoBKSZJGYEPBwCX+-BQEF4BQGKQ0BScdyJgOPrYDVIuAmOgQJZZiD46cVMgXFQoEc0uou8Wgavy4CQxPw1EF-klj6AuB8ICeMYOMgY7mp3SikHbk+RbLn8Xg7+OOmABjBh0o0WGDmOTEYLv4lQPQXLkqBiieAXmWOTgLvXUHBCT6UdPAdfWIEmDo609LxAfRxQxh7B1BKSO-gwAC0BQdgrKNzhiGwNRy4HLoEkN7w9IEhzQ5IXQJTglDahnyHoRQGWi2ZuccA-odNlGGlAYwd0F-l0JwoQMia4QR9I4PL5cp3AowHTAxz5i-IO6CwBuq-1QQO4iCtnPyLREgbE1VhPQMmuwKrQzE1Is8CLCcPmEk01hlwgIYMUCa7wZhFZPCiH1gLQMDm6BTIN-QYipodIc3NBhwxTreI-Y7ANCDAwBEuAgRD+CjCg1LbGU7qK7VYJQI+hg1LalDJwDGA-pf0EGYQaQWElgGr9OG0IiALCP+FTgERxIpEW7hRG3kp2JlXbmsCxHrEtkZuPEe-Soa8MSRiSM8GCXkF7whEQAA)

## Acknowledgements

Many thanks to the creators, contributors, and maintainors for making these powerful tools available for free: 

- Python
- PyShiny
- GitHub
- pandas
- plotly
- numpy
- scipy
- statsmodels
- scikit-learn

## Screenshot Example 1

![Example 1](images/example1.png)

## Screenshot Example 2 (Dataset 1)

![Example 2](images/example2-dataset1.png)

## Screenshot Example 2 (Dataset 2)

![Example 2](images/example2-dataset2.png)

## Historical Note

Back in his 1970 [book](images/README.md), "Statistical Problems and How To Solve Them", L.H. Longley-Cook noted (as a footnote on page 153):

"The least squares line in not completely satisfactory because it gives too great a weight to extreme values. 
Some writers have proposed the least distance line, when |D1| + |D2| + |D3| + |D4| + ... is a minimum.
|D| is the distance taken as positive in each case.
In the past, it has been difficult to caclulate this line because of the sign problem, but this can be overcome with modern computers."

That was 50 years ago. Why are we still avoiding "difficult" absolute value calculations by squaring?
