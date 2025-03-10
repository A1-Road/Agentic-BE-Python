# Agentic-BE-Python

**English** | [日本語](#japanese)

Agentic-BE-Python is the backend component of the Agentic project built using the [FastAPI](https://fastapi.tiangolo.com/) framework. It is a server that accepts requests from Agentic-BE-TS.

## Endpoints

- **POST** `/parse_instruction`: Parses transaction instructions.
- **GET** `/check_reputation`: Checks the reputation of an Ethereum address.  
For more details, please refer to [this page](https://cooperative-chive-de7.notion.site/API-Endpoints-1ab0382e4479809d9305df9cde8ed5ef?pvs=4).

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/A1-Road/Agentic-BE-Python.git
   cd Agentic-BE-Python
   ```

2. **Install dependencies:**

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Create the env files:**

   ```bash
   cp .env.template .env
   cp src/env.template.py src/env.py
   ```

   Modify the variables as needed.

4. **Install the VSCode extension:**
   - Black Formatter

## How to Run

Run the server using the following command:

```
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

Once the server is running, you can test the API using Swagger UI at `http://localhost:8000/docs`.

## Script Explanation (Not Updated)

### `parse_instruction.py`

This script parses the details of an Ethereum transaction entered by the user and generates output in a specified format.

#### Input

The user provides a prompt containing details of an Ethereum transaction. For example:

```plaintext
Send 0.0005 ETH to 0xA2dBbc0EAE6c0402BF2E59d5A100dD7C9395539a
```

#### Output

Based on the input prompt, the script generates transaction information and returns an output similar to:

```json
{
    "amount": 0.0005,
    "who": "0xA2dBbc0EAE6c0402BF2E59d5A100dD7C9395539a"
}
```

#### Script Flow

1. Import necessary libraries and load environment variables.
2. Instantiate the `ChatOpenAI` model.
3. Define a Pydantic model called `EthTransaction`.
4. Create a `PydanticOutputParser`.
5. Generate formatting instructions.
6. Set up the prompt template.
7. Create and execute the langchain.

Below is the main part of the script:

```python
# filepath: /workspaces/codespaces-jupyter/Agentic/backend/fetch_wallet_data.py
// ...existing code...
```

### `check_reputation.py`

This script checks the reputation based on a given command and returns the result.

#### Input

The user inputs a command to check reputation. For example:

```plaintext
Check the reputation of 0xA2dBbc0EAE6c0402BF2E59d5A100dD7C9395539a
```

#### Output

Based on the input command, the script generates reputation information and returns output such as:

```json
{
    "output": true
}
```

#### Script Flow

1. Import necessary libraries and load environment variables.
2. Instantiate the `CdpAgentkitWrapper`.
3. Create the `CdpToolkit`.
4. Instantiate the `ChatOpenAI` model.
5. Create and execute the agent.
6. Configure and run the Flask application.

Below is the main part of the script:

```python
# filepath: /workspaces/codespaces-jupyter/Agentic/backend/in_progress_takara/check_reputation.py
// ...existing code...
```

## How to Run the Scripts

1. Install the necessary libraries.
2. Create a `.env` file and set the required environment variables.
3. Run the script:

```bash
python fetch_wallet_data.py
```

or

```bash
python check_reputation.py
```

This script parses the details of the command input by the user and generates output following the specified format.

---

# Japanese

[English](#agentic-be-python) | **日本語**

Agentic-BE-Pythonは、[FastAPI](https://fastapi.tiangolo.com/)フレームワークを使用して構築されたAgenticプロジェクトのバックエンドコンポーネントです。
Agentic-BE-TSからのリクエストを受け付けるサーバーです。

## エンドポイント

- POST `/parse_instruction`: トランザクション指示を解析します
- GET `/check_reputation`: Ethereumアドレスの評判をチェックします
詳細は[こちら](https://cooperative-chive-de7.notion.site/API-Endpoints-1ab0382e4479809d9305df9cde8ed5ef?pvs=4)です。

## セットアップ

1. **リポジトリをクローンする：**

   ```bash
   git clone https://github.com/A1-Road/Agentic-BE-Python.git
   cd Agentic-BE-Python
   ```

2. **依存関係をインストールする：**

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **envファイルを作成する：**

   ```bash
   cp .env.template .env
   cp src/env.template.py src/env.py
   ```

   各変数を書き換えて下さい。

4. **VSCodeの拡張機能をインストールする**
   - Black Formatter

## 実行方法

```
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

サーバーが起動したら、`http://localhost:8000/docs` でSwagger UIを通じてAPIをテストできます。

## スクリプトの説明（未更新）

### `parse_instruction.py`

このスクリプトは、ユーザーが入力したEthereumトランザクションの詳細を解析し、指定されたフォーマットに従って出力を生成します。

### 入力

ユーザーは、Ethereumトランザクションの詳細を含むプロンプトを入力します。例えば、以下のような入力があります：

```plaintext
Send 0.0005 ETH to 0xA2dBbc0EAE6c0402BF2E59d5A100dD7C9395539a
```

### 出力

スクリプトは、入力されたプロンプトに基づいてトランザクション情報を生成し、以下のような出力を返します：

```json
{
    "amount": 0.0005,
    "who": "0xA2dBbc0EAE6c0402BF2E59d5A100dD7C9395539a"
}
```

### スクリプトの流れ

1. 必要なライブラリのインポートと環境変数の読み込み。
2. `ChatOpenAI` モデルのインスタンス化。
3. `EthTransaction` というPydanticモデルの定義。
4. `PydanticOutputParser` の作成。
5. フォーマット指示の生成。
6. プロンプトテンプレートの設定。
7. langchainの作成と実行。

以下は、スクリプトの主要部分です：

```python
# filepath: /workspaces/codespaces-jupyter/Agentic/backend/fetch_wallet_data.py
// ...existing code...
```

### `check_reputation.py`

このスクリプトは、コマンドに基づいて評判をチェックし、結果を返します。

### 入力

ユーザーは、評判をチェックするためのコマンドを入力します。例えば、以下のような入力があります：

```plaintext
Check the reputation of 0xA2dBbc0EAE6c0402BF2E59d5A100dD7C9395539a
```

### 出力

スクリプトは、入力されたコマンドに基づいて評判情報を生成し、以下のような出力を返します：

```json
{
    "output": true
}
```

### スクリプトの流れ

1. 必要なライブラリのインポートと環境変数の読み込み。
2. `CdpAgentkitWrapper` のインスタンス化。
3. `CdpToolkit` の作成。
4. `ChatOpenAI` モデルのインスタンス化。
5. エージェントの作成と実行。
6. Flaskアプリケーションの設定と実行。

以下は、スクリプトの主要部分です：

```python
# filepath: /workspaces/codespaces-jupyter/Agentic/backend/in_progress_takara/check_reputation.py
// ...existing code...
```

## 実行方法

1. 必要なライブラリをインストールします。
2. `.env` ファイルを作成し、必要な環境変数を設定します。
3. スクリプトを実行します。

```bash
python fetch_wallet_data.py
```

または

```bash
python check_reputation.py
```

このスクリプトは、ユーザーが入力したコマンドの詳細を解析し、指定されたフォーマットに従って出力を生成します。