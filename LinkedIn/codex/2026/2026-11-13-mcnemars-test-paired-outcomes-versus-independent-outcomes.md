# McNemar’s Test: When to use and when not

📊 A pass rate rises from 45% to 55% after a treatment. Which statistical test should you use?
Or how will test one ML classifier's sensitivity is higher than another ML classifier?

Start with the study design: were these the same people measured twice, or two independent groups?

🔗 For paired binary outcomes, McNemar’s test focuses on the people whose outcomes changed. In my example of 100 people:

| Before treatment | After: pass | After: fail | Total |
| --- | ---: | ---: | ---: |
| Pass | 40 | 5 | 45 |
| Fail | 15 | 40 | 55 |
| Total | 55 | 45 | 100 |

The exact McNemar p-value is about 0.041. Discarding the pairing and applying Fisher’s exact test gives about 0.203—an inappropriate analysis for this paired comparison.

🔍 Another subtle trap: applying Fisher’s test directly to the paired transition table tests association between before and after outcomes. It answers a different question from whether the overall pass probability changed.

💡 Choose the right test based on the study design and the question. Even an exact calculation needs the right sampling model.

👉 Read the explanation and Python examples:
https://fortune9.netlify.app/2026/11/13/mcnemars-test-paired-outcomes-versus-independent-outcomes/

#Statistics #DataScience #Python #McNemarsTest #StudyDesign
