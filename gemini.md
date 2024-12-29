# GitHub Actions Workflow: `apimtest.yml`

## Purpose
The `apimtest.yml` file is a GitHub Actions workflow configuration designed to automate the testing of the `GeminiAI` class whenever changes are pushed to the `main` branch or a pull request is created. This ensures that the code is tested in a consistent environment.

## Workflow Triggers
The workflow is triggered by the following events:
- **Manual Dispatch**: Can be manually triggered via the GitHub Actions interface.
- **Push to Main Branch**: Runs when changes are pushed to the `main` branch.
- **Pull Request to Main Branch**: Runs when a pull request is created targeting the `main` branch.
- **Path-Specific Changes**: Runs when changes are made to files in the `gemini/**` directory or the `.github/workflows/apimtest.yml` file.

## Job: `test`
The workflow defines a single job named `test` that runs on an `ubuntu-latest` runner and targets the `Dev` environment.

### Steps
1. **Checkout Code**
   - Uses `actions/checkout@v3` to checkout the repository code.
   ```yaml
   - uses: actions/checkout@v3
2. **Set up Python**

   - Uses actions/setup-python@v4 to set up Python 3.10.
3. **Create .env file**

   - Creates a .env file with the necessary environment variables for the tests.

   ```yaml
   - name: Create .env file
     run: |
       echo "GEMINI_API_KEY=${{ secrets.GOOGLE_API_KEY }}" > gemini/.env
       echo "AZURE_APIM_ENDPOINT=${{ vars.AZURE_API_URL }}" >> gemini/.env
       echo "AZURE_APIM_SUBSCRIPTION_KEY=${{ secrets.AZURE_API_KEY }}" >> gemini/.env
      
    ```

4. **Install Python dependencies**

```yaml
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install google-generativeai python-dotenv requests

```
5. **Run Tests**

Runs the unit tests using unittest.

```yaml
- name: Run tests
  run: |
    cd gemini
    python -m unittest test.py -v
```

## Criteria

This tests 2 scenaros, where one test directly calls the gemini service to see, if it's able to get a successful response.

The next one calls the same gemini service but only via API management. This enables the developer to track / log / throttle the api requests and response in the API management itself.