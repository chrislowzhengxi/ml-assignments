# Final Exam Generation Instructions

## Original Prompt

generate a final exam for this course. 1. roughly follow the format and question balance from previous finals here (https://github.com/noise-lab/security-course/tree/master/docs/final) 2. focus on topcs in meetins 7 amd 8 here (https://github.com/noise-lab/security-course/blob/master/docs/agenda.md) 3. there are some instructions in the midterm directory, generate-mideterm.md, which you should definitely follow as far as formatting, question design, point totals, etc. as a starting point. 4. in particular, focus on question design: plenty of multiple choice questions, yes/no questions with text boxes that allow students to explain why or why not, etc. 5. when you are done, please also include in the final directory not only a draft of the final in final/2025/ but also a copy of this prompt verbatim, to help students generate practice exams. also generate a generate-final.md file that encodes all of the instructions that we eventually use and put that into final/generate-final.md.

Additional requirements:
(1) be sure to include solutions using the solutions macro so we can turn those on/off
(2) DO NOT CHECK INTO GITHUB

---

## Exam Specifications

- **Total Points**: ~60-65 points (based on analysis of 2023 and 2024 finals)
- **Format**: Multiple choice, short answer, yes/no with explanation, and case study questions
- **Margins**: 0.5 inches (all sides)
- **Solutions**: Use solution macros to enable/disable answers

## Coverage

The final exam covers material from **Meetings 7-8** according to the course agenda:

### Meeting 7: Privacy Law and Regulation
1. **Historical Context**: Warren & Brandeis, FIPPs (Fair Information Practice Principles)
2. **US Privacy Law**: Sectoral approach, major statutes (HIPAA, COPPA, etc.), HIPAA gap
3. **FTC Enforcement**: Section 5, major settlements
4. **GDPR**: Extraterritorial reach, key requirements, enforcement examples
5. **Core Privacy Principles**: Notice, consent, opt-in vs opt-out

### Meeting 8: Compliance, Dark Patterns, AI Privacy, and Copyright
1. **CCPA/CPRA**: Requirements, timelines, GPC (Global Privacy Control)
2. **Automated Compliance**: Spillover effect, compliance challenges
3. **Dark Patterns**: Three categories (obstruction, interface interference, misdirection)
4. **AI Privacy**: Memorization, interdependent privacy, anthropomorphization
5. **Copyright and Fair Use**: Four tests, transformative use, AI litigation

## Question Types and Distribution

### Multiple Choice (Select All That Apply)
- **Count**: 8-9 questions
- **Points**: 4 points each
- **Total**: 32-36 points
- Use `\prob{4}` to start question
- Use `\correctanswercircle{text}` for correct answers
- Use `\answercircle{text}` for incorrect answers
- Clearly indicate "Select all that apply" in question text

### Yes/No Questions with Explanation
- **Count**: 3 questions
- **Points**: 4 points (yes/no) + 3 points (explanation) = 7 points total
- Use `\yesnoyes` or `\yesnono` for the yes/no answer
- Follow with explanation using `\answerbox{height}{solution}`
- Note: Some yes/no questions may be 4 points standalone

### Short Answer Questions
- **Count**: 4-5 questions
- **Points**: 3 points each
- **Total**: 12-15 points
- Use `\answerbox{height}{solution}` for answer boxes
- Typical heights: 1.25-2.0 inches
- Solutions should be 2-4 sentences

### Case Study Questions
- **Count**: 2-3 case studies with associated questions
- Use `\framebox` and `\parbox` for case study formatting
- Include scenarios for dark patterns, fair use arguments, ethics

### Feedback Questions
- **Count**: 2 questions
- **Points**: 1-3 points total
- Interest/difficulty ratings + open feedback

## Formatting Guidelines

### Page Breaks
- Use `\newpage` strategically to control pagination
- Break between major sections when appropriate

### Vertical Spacing
- Add `\vspace*{-0.1in}` before section headings to save space
- Use negative vspace (`\vspace*{-0.15in}` to `-0.25in`) before large elements

### Section Headings
- Use `\section*{Topic Name}` for major sections
- Topics: Privacy Law and Regulation, GDPR and International Privacy, CCPA/CPRA and Automated Compliance, Dark Patterns, AI and Privacy, Copyright and Fair Use

### Case Studies
```latex
\begin{center}
\framebox[0.9\linewidth]{
\parbox{0.8\linewidth}{
    {\bf Case Study:}
    Case study text...
}
}
\end{center}
```

## File Structure

- `exam.tex` - Main file with document class and geometry settings
- `instructions.tex` - Exam instructions and name acknowledgment
- `questions.tex` - All exam questions
- `feamster.sty` - Style file for exam formatting (copied from midterm)
- `Makefile` - Build system for both student and solution versions (copied from midterm)

## Building the Exam

```bash
make exam      # Builds student version (exam.pdf)
make solution  # Builds solution version (exam-solution.pdf)
make clean     # Removes auxiliary files
```

## Key Requirements

1. **Follow formatting from generate-midterm.md** - Use same macros, spacing, and structure
2. **Focus on Meetings 7 and 8 topics** - Privacy law, GDPR, CCPA/CPRA, dark patterns, AI privacy, copyright
3. **Include solutions using macros** - All answers in `\answerbox{}`, `\correctanswercircle{}`, etc.
4. **Balance question types** - Mix of multiple choice, short answer, yes/no, and case studies
5. **Use case studies for application** - Especially for dark patterns and fair use arguments
6. **Total ~60-65 points** - Consistent with previous final exams
7. **Do not check into GitHub** - Local development only

## High-Priority Topics (From Meeting Notes)

### Dark Patterns (Very Likely)
- Three categories: obstruction, interface interference, misdirection
- Examples in privacy opt-out contexts
- OneTrust compliance paradox

### Copyright Fair Use (Very Likely)
- Four fair use tests (purpose/character, nature, amount, market effect)
- Transformative use definition and examples
- Argue FOR and AGAINST fair use in AI scenarios
- What can/cannot be copyrighted

### AI Privacy (High Priority)
- Traditional vs AI-specific privacy risks
- Memorization and prompt injection
- Interdependent privacy problem
- Anthropomorphization and progressive disclosure
- Dark patterns in LLM interfaces

### Privacy Regulation (Moderate-High Priority)
- CCPA/CPRA requirements, dates, covered entities
- Spillover/California effect
- GPC (Global Privacy Control)
- FIPPs limitations in modern context
- GDPR extraterritorial reach
- HIPAA gap

## Point Distribution Guidelines

- Multiple choice (select all that apply): 4 points
- Multiple choice (select one): 3 points
- Short answer: 3 points
- Short answer with explanation: 2-3 points
- Yes/No: 4 points
- Yes/No explanation: 3 points (7 points total with yes/no)
- Feedback: 1-2 points

## Content Notes

### Important Distinctions
- FIPPs assume static databases; modern systems use ML and inference
- US uses sectoral approach; EU uses omnibus approach (GDPR)
- Traditional privacy risks vs AI-specific risks
- Link presence ≠ link functionality in compliance

### Case Law and Examples
- Recent FTC settlements: Amazon Prime, BetterHelp, GoodRx
- GDPR fines: Meta €1.2B, Amazon €746M
- Google v. Oracle (transformative use)
- Authors v. AI companies (ongoing litigation)

### Likely Question Formats
1. Identify dark pattern category from interface example
2. Construct fair use argument FOR transformative use
3. Construct fair use argument AGAINST based on market harm
4. Explain HIPAA gap with examples
5. Describe spillover effect in privacy compliance
6. Explain interdependent privacy in LLM context
7. Analyze LLM interface for dark patterns
