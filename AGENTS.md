# AGENTS.md Template

Use this template as a starting point for projects that rely on agents. Customize the
sections to reflect your repo's conventions and tooling. Delete any sections that don’t
apply.

## Scope

- `/agents/` – core agent logic
- `/configs/` – YAML/JSON agent configuration files
- `/scripts/` – utilities for training, evaluation, or deployment

## Environment Setup

- Use `pyenv` or `conda` to manage Python versions.
- Create a virtual environment:
  python -m venv .venv && source .venv/bin/activate
- Install dependencies:
  pip install -r requirements.txt
- For reproducibility, also update `requirements.lock` or `poetry.lock`.
- For AI Agent Functionality: Requires a working internet connection to interact with the Gemini API and Firebase Firestore.

### Common Cases 

- **LangChain**:
  pip install langchain openai
- **Hugging Face Transformers**:
  pip install transformers datasets accelerate
- **OpenAI SDK**:
  Requires `OPENAI_API_KEY` in `.env`. Example:
  export OPENAI_API_KEY=sk-...
- **Docker**:
  docker build -t my-agent .
  docker run -it --env-file .env my-agent

## Code Style

- **Python** – run `black` and `isort` on all `.py` and `.ipynb` files.
- **Bash** – lint scripts with `shellcheck`.
- **Rust** – run `cargo clippy --workspace --all-targets -- --deny warnings`.
- **Markdown/Docs** – check with `markdownlint` or `prettier`.

## Testing

Outline how to validate changes. Examples:
- pytest with coverage reporting (`pytest --cov=agents`)
- python -m py_compile $(git ls-files '*.py')
- npm test if JavaScript utilities are included
- Integration tests for end-to-end agent workflows (`tests/integration/`)

### Common Cases

- **Mocking LLMs** – use fixtures to stub API calls (`responses`, `vcrpy`, or `pytest-mock`).
- **Golden Files** – store expected agent outputs in `/tests/golden/`.
- **CI/CD** – GitHub Actions workflows (`.github/workflows/test.yml`) run lint + test.

## Evaluation

- Document metrics used to assess agents (e.g., task success rate, accuracy, reward).
- Store evaluation scripts under `/evaluation/` and update benchmark results in `EVAL.md`.
- Use fixed random seeds for reproducibility.

### Common Cases 

- **LangChain Benchmarks** – see `/evaluation/langchain_eval.py`.
- **HF Leaderboards** – push metrics to Hugging Face `datasets`.
- **Human-in-the-Loop** – use structured annotation tasks for subjective evaluation.

## Deployment

- Provide example commands or configs for local runs:
  python agents/run.py --config configs/example.yaml
- Document any containerization (e.g., `Dockerfile`) and cloud workflows.
- Mention orchestration tooling (e.g., `tmux`, `Ray`, `Kubernetes`) if applicable.

### Common Cases 

- **Streamlit UI**:
  streamlit run ui/app.py
- **Gradio Demo**:
  python ui/gradio_demo.py
- **FastAPI Server**:
  uvicorn api.main:app --reload

## Pull Request Checklist

1. Update relevant documentation (`README.md`, `AGENTS.md`, `EVAL.md`).
2. Include citations for code and terminal output where required.
3. Ensure the working tree is clean before requesting review.
4. Verify that all pre-commit hooks and CI tests pass.

## Notes for Contributors

- Prefer fully qualified imports (`import transformers`) over `from` imports.
- Log prompts and model outputs when debugging agents.
- Mention any required environment variables, keys, or services (see `.env.example`).
- Use `logging` instead of `print` for consistent logs.
- Keep configuration values in `.yaml` or `.json` files—avoid hard-coding.

### Common Cases )

- **Logging**: use `structlog` or `loguru` for structured logging.
- **Telemetry**: integrate with `wandb`, `mlflow`, or `tensorboard`.
- **Secrets**: manage via `.env`, `doppler`, or `gcloud secrets`.

## Troubleshooting

- **Common errors** – list frequent issues (e.g., missing API keys, CUDA setup problems).
- **Debugging tips** – how to reproduce a failing agent run with verbose logging.
- **Support** – link to project Slack/Discord channel or GitHub Discussions.
