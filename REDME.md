# GitGrade – Intelligent GitHub Repository Evaluator

## Theme
AI + Code Analysis + Developer Profiling

## Problem Statement
A GitHub repository represents a developer’s real skills, but most students do not know how clean, complete, or recruiter-ready their code is. GitGrade is an intelligent system that evaluates a public GitHub repository and converts it into a meaningful **Score**, **Summary**, and **Personalized Improvement Roadmap**.

The system acts as a **Repository Mirror**, reflecting the true strengths and weaknesses of a project based entirely on real repository data.

---

## Objective
To design an AI-powered system that:
- Accepts a public GitHub repository URL
- Automatically fetches repository data
- Evaluates the repository on multiple quality dimensions
- Generates honest and actionable feedback for improvement

---

## System Architecture

### 1. Repository Data Fetching
GitGrade uses the GitHub REST API to collect publicly available repository data such as:
- File and folder structure
- Programming languages used
- Commit history
- README presence
- Test folder presence
- Basic repository metadata

This ensures that the evaluation is based on **real, verifiable data** rather than assumptions.

---

### 2. Automated Repository Analysis
The fetched data is analyzed across multiple dimensions:
- Code structure and organization
- Documentation quality
- Testing and maintainability
- Git commit consistency
- Language and technology usage

---

### 3. Scoring Mechanism
Each repository is scored on a **0–100 scale** using weighted indicators such as:
- README availability
- Test presence
- Commit count
- Folder organization
- Language usage
- Repository activity

The final score is mapped to a developer level:
- **0–40** → Beginner
- **41–70** → Intermediate
- **71–100** → Advanced

---

### 4. AI-Inspired Evaluation & Roadmap
Based on the repository analysis, GitGrade generates:
- A concise written summary describing repository quality
- A personalized improvement roadmap with actionable steps

The roadmap feels like guidance from an AI coding mentor, helping developers improve their real-world coding practices.

---

## Output Format

### Score / Rating
Example:
Score: 78 / 100  
Level: Intermediate

### Written Summary
A short, honest evaluation highlighting strengths and weaknesses of the repository.

### Personalized Roadmap
Actionable steps such as:
- Improving folder structure
- Adding a detailed README
- Writing unit tests
- Following Git best practices
- Adding CI/CD pipelines

---

## Project Structure
