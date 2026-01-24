<<<<<<< HEAD
# Tunisia-AI-Tour-2026---AJIZ-Zarzis-Pitstop---Agentic-AI-Workflows-on-Google-Vertex-AI-Workshop
=======
# DevFest Istanbul Türkiye 2025

Building Agentic AI Systems with xAI on Vertex AI   
From Perception to Action + Agent Builder Comparison**

**Author: Manai Mohamed Mortadha**


---

## **Overview**

This repository contains the full demos, code, and materials used in my **DevFest Istanbul Türkiye 2025** session.
The talk covers two major parts:

### **Part I — Building Agentic AI Workflows with xAI on Vertex AI**

A complete deep dive into designing and deploying enterprise grade autonomous AI agents capable of:

• Perceiving external data
• Reasoning with ML models
• Acting autonomously
• Explaining their decisions using xAI techniques
• Running reliably and scalably on Google Cloud Vertex AI

The demo replicates real production pipelines I have designed in industry, including projects at Netflix, MAN.AI, and work I have evaluated as an AI consultant for Tegus.

---

### **Part II — Rebuilding the Same Agent Using Vertex AI Agent Builder**

A second version of the workflow shows how the same agent can be redesigned with **Vertex AI Agent Builder** (formerly Vertex AI Search + Conversations), offering:

• Easier development
• Declarative logic
• Native tool calling
• LLM powered orchestration
• Built in safety and grounding

This section helps developers understand **when to choose custom agentic pipelines** and **when to choose Agent Builder’s rapid development approach**.

---

# **Session Summary**

Agentic AI systems are becoming the core of modern enterprise automation.
They follow a structured loop:

• Collect
• Interpret
• Predict
• Decide
• Act
• Explain
• Log

In this session, you will learn how to build this full loop using:

• Vertex AI Pipelines
• Model Registry
• Endpoints for real time inference
• xAI interpretability tools (SHAP, Feature Attributions)
• RAG enabled retrieval
• Automated controlled actions
• Cloud Logging and BigQuery audit trails

At the end, the same agent is rebuilt using **Agent Builder**, demonstrating a simpler low code approach.

---

# **Session Agenda**

## **1. Introduction**

• Why agentic AI matters now
• Real world use cases across finance, retail, health, and cloud platforms
• Trust, transparency and why xAI is necessary in autonomous systems

---

## **2. What Is an AI Agent**

• Core components
• Perception to action loop
• State management
• Policies and guardrails
• How xAI is integrated

---

## **3. Vertex AI Deep Dive**

• Workbench for development
• Training and registry
• Endpoints for interactive inference
• xAI built in explainable predictions
• Deploying reliable cloud scale decision systems

---

## **4. Designing Agentic Pipelines (Full Custom Build)**

• Connecting data sources
• Event driven triggers
• Multi step reasoning
• Automated actions with control logic
• Model supervision and human in the loop

---

## **5. Adding xAI Layers**

• Why explanations matter in enterprise
• SHAP
• Vertex AI Feature Attribution
• Generating text explanations
• Storing transparent audit trails

---

## **6. Using Vertex AI Models + RAG**

• Bringing context into decisions
• Hybrid predictive plus retrieval reasoning
• Feedback loops and improvement cycles

---

## **7. Live Demo: Building the Full Agent**

• Train the model
• Integrate perception → reasoning → action
• Generate explanations
• Produce logs
• View the full workflow end to end

---

## **8. Part II — Same Agent with Vertex AI Agent Builder**

In this part we rebuild the agent using Agent Builder:

• Declarative agent creation
• Built in grounding
• Prompt orchestration
• Tool calling and actions
• Workflow orchestration
• Safety filters

We compare both approaches to help developers choose the right path for their company.

---

# **Demo 1

Manually Built Agentic AI System with xAI**

This folder contains a complete manually engineered agentic pipeline representing enterprise applications I have deployed in practice.

---

# **What the Agent Does**

## **1. Collects Information**

Uses a mock API simulating customer activity.
Real world analogs include:

• Event streams
• CRM logs
• Retail metrics
• Sensor readings
• Financial flows

---

## **2. Analyzes Input**

Loads a trained model:

```
vertex_model.pkl
```

Predicts user behavior or likelihood of positive action.

---

## **3. Explains Its Reasoning**

Using SHAP, the agent generates both:

• Visual explanations
• Textual reasoning summaries

Files saved inside:

```
outputs/explanations/
```

---

## **4. Acts Autonomously**

Outputs may include:

• Sending notifications
• Updating databases
• Triggering follow up tasks
• Or deciding no action is needed

---

## **5. Audit Logging**

Every cycle is logged:

```
outputs/audit_logs/
```

Contains:

• Inputs
• Predictions
• Explanations
• Actions
• Timestamps

Perfect for enterprise compliance.

---

# **Why This Is an Agentic AI System**

| Component      | Description                   |
| -------------- | ----------------------------- |
| Perception     | Pulls external data           |
| Reasoning      | ML driven decision logic      |
| Explainability | Transparent SHAP attributions |
| Action         | Real autonomous output        |
| Logging        | Full history for trust        |

This matches architectures used in:

• Netflix personalization
• MAN.AI enterprise automation tools
• Fintech and retail clients in Tegus consultations
• Research workflows at Saint Mary’s University

---

# **Repository Structure**

```
devfest-istanbul-agent-demo/
├── agent_custom/
│   ├── agent_demo.py
│   ├── train_model.py
│   ├── mock_api.py
│   └── outputs/
│       ├── audit_logs/
│       └── explanations/
├── agent_builder_version/
│   ├── builder_config.json
│   ├── tool_definitions.json
│   └── example_queries.md
└── README.md
```

---

# **Running the Custom Agent**

## **1. Install dependencies**

```bash
pip install -r requirements.txt
```

## **2. Train the model**

```bash
python train_model.py
```

## **3. Run the agent**

```bash
python agent_demo.py
```

---

# **Mapping to Vertex AI**

| Local Version    | Vertex AI Equivalent             |
| ---------------- | -------------------------------- |
| train_model.py   | Vertex AI Training               |
| vertex_model.pkl | Vertex Registry                  |
| agent_demo.py    | Pipelines + CloudRun + Functions |
| SHAP             | Vertex Explainable Predictions   |
| mock API         | Pub Sub / CRM Events             |
| audit logs       | Cloud Logging + BigQuery         |

---

# **Part II

Simplifying with Vertex AI Agent Builder**

This folder shows:

• How to recreate the same agent using Agent Builder
• How the system becomes declarative
• How actions are implemented through tools
• How grounding improves reliability
• How LLMs handle the orchestration logic

This demonstrates the evolution from a **fully custom engineering pipeline** to a **low code enterprise grade platform** suitable for faster productionization.

---

# **Speaker**

**Eng. Manai Mohamed Mortadha**
Senior AI Engineer | Netflix
PhD Candidate in Explainable AI | SAINT MARY'S UNIVERSITY
AI Expert Consultant | Tegus
CEO & Head of AI R&D | MAN.AI
International AI Speaker
AI Expert Reviewer & Author | Packt Publishing UK

---

# **Connect**

**Website**
[https://taplink.cc/manaimortadha](https://taplink.cc/manaimortadha)

**LinkedIn**
[https://linkedin.com/in/mannai-mortadha](https://linkedin.com/in/mannai-mortadha)

**GitHub**
[https://github.com/MortadhaMannai](https://github.com/MortadhaMannai)

**Email**
[mannaimortadha898@gmail.com](mailto:mannaimortadha898@gmail.com)


>>>>>>> 9b59814f33a1ddd53f4268da5cba80fdaf8ade25
# Tunisia-AI-Tour-2026---AJIZ-Zarzis-Pitstop---Agentic-AI-Workflows-on-Google-Vertex-AI-Workshop
