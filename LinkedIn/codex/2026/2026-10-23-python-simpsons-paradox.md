# Simpson’s Paradox: Confounder Variable Can Reverse the Story

🤔 Can program A have a higher exam pass rate than program B at every difficulty level—and still have a lower pass rate overall?

Yes. That’s Simpson’s paradox: an association that holds within each subgroup can reverse when the groups are combined.

🔬 In my latest blog post, I demonstrate this with a simulation of 20,000 students passing exams:

📚 On both easy and hard exams, program A has the higher pass rate.
📊 When all students are combined, program B comes out ahead.

Why? Most students in A take hard exams, while most students in B take easy exams. The overall rates are weighted averages, and the two programs have very different group compositions.

💡 The lesson: examine group sizes as well as rates. An overall comparison can tell a different story from comparisons within groups.

Deciding what to adjust for still requires understanding how the variables relate; adding every variable is not a general solution.

👉 Read the simulation, visual explanation, and logistic regression results:
https://fortune9.netlify.app/2026/10/23/python-simpsons-paradox/

#Statistics #SimpsonsParadox #Python #DataScience #Confounding
