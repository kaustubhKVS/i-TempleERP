# The "transaction confirmation" a "NFT"? More info on "Creating one NFT per transaction"...? Is this confirmation just a hash?
While engaging in decentralized application development, I've established a coding principle, endorsed by Dr Sadoghi from the ResDB Lab, that facilitates the conversion of any centralized application into a decentralized one. This involves the transformation of a conventional SQL-based context into a Blockchain framework.

Let's delve into the process with step-by-step examples:

1. **Identify Centralized Transaction Data:**
   - Original Data: Consider a transaction recorded in a centralized system, comprising information like Name, Amount, and Occasion.
     ```sql
     INSERT INTO TransactionData (Name, Amount, Occasion) VALUES ('John Doe', 100.00, 'Purchase');
     ```

2. **Map Transaction to NFT:**
   - Transformation: Convert each transaction into a unique NFT (Non-Fungible Token) in the Blockchain.
     ```json
     {
       "Name": "John Doe",
       "Amount": 100.00,
       "Occasion": "Purchase"
     }
     ```

3. **Blockchain Ledger:**
   - Record the transaction information by minting an NFT in the Blockchain ledger.
     ```python
     # Example using a Blockchain library
     blockchain.mint_nft({
       "Name": "John Doe",
       "Amount": 100.00,
       "Occasion": "Purchase"
     });
     ```

4. **Inspiration from MongoDB:**
   - Draw inspiration from MongoDB's document-oriented approach for data storage.
     ```json
     // MongoDB Document
     {
       "_id": ObjectId("5f3f1fe5c20dfb6f162b3a65"),
       "Name": "John Doe",
       "Amount": 100.00,
       "Occasion": "Purchase"
     }
     ```

5. **Decentralized Ledger Database:**
   - Treat the collection of NFTs in the Blockchain as a decentralized ledger database.
     ```python
     # Example treating Blockchain as a decentralized ledger database
     decentralized_ledger.query({
       "Name": "John Doe"
     });
     ```

In this approach, each transaction recorded results in the minting of an NFT containing relevant information (Name, Amount, Occasion) in the Blockchain ledger. This methodology is inspired by MongoDB's document-centric storage, where each entry is stored as a file document with its properties in a single file, forming a collection of files treated as a database.

# Use of General US survey to make predictions for Indian temple
The predictive model, utilizing Meta's Prophet, is designed to forecast the number of visitors to a temple on a specific day. In the absence of direct data from the Indian context, a pragmatic approach was taken by leveraging data from a US survey that monitored attendance at social gatherings in the United States. This dataset was employed as the training data for a rapid proof-of-concept.
Let's break down the steps and considerations:

1. **Choice of Predictive Model:**
   - Utilizing Meta's Prophet as the predictive model for forecasting visitor numbers at the temple.

2. **Data Source:**
   - Lack of direct data from the Indian context prompted the use of an alternative dataset.
   - The US Survey data on attendance at social gatherings in the United States was chosen as a substitute.

3. **Training Data:**
   - The US Survey data became the primary source for training the predictive model.
     ```python
     # Example loading and preparing US Survey data for training
     us_survey_data = load_us_survey_data()
     model.train(us_survey_data)
     ```

4. **Proof-of-Concept:**
   - The US Survey data was employed as a substitute to quickly demonstrate the feasibility and functionality of the predictive model.
     ```python
     # Example demonstrating a proof-of-concept with the US Survey data
     predictions = model.predict(us_survey_data)
     ```

5. **Adaptation to Indian Context:**
   - While the US Survey data served as a temporary solution, future iterations of the model may require adaptation to the specific characteristics of the temple and its surroundings in India.

By leveraging the US Survey data as a proxy for the Indian context, this approach allowed for the rapid development of a proof-of-concept using Meta's Prophet to predict the number of visitors to the temple on a given day. However, it's essential to keep in mind that the model may need further refinement and customization as more relevant data becomes available for the Indian context.

# Azure OpenAI ChatGPT Studio for LLM: Is this a pretrained LLM? What do the Bhagwad Geeta quotes do? "PDF from the internet" do and what does it consist of? Can you show it's limits?
I have not finetuned ChatGPT as it would cost me a huge amount of financial resources.
Using the Azure OpenAI Studio, we can customise the behaviour using prompt engineering and Retrivel Augmented Generation (RAG) which is the production ready industry standard for context aware LLM response.

Prompt Engineering :I have configured the behavior of the ChatGPT to be a religious scholar assistant for answering questions of piligrims. I performed this by using Few-Shot Learning techniques which means giving examples of responses we expect form ChatGPT. Bhagwad Geeta was used as a few-shot learing example. I also paid special attention to negetive prompts which help in restricting what ChatGPT should NOT say in a conversation.

RAG : This technique is crucial for context aware responses. RAG works on a managing an LLM over document/data configured for context-aware response.
Process Flow of RAG Looks like this :
Document/ Data used : Wikipedia articles and 2 articles based on Mahur as PDF.

1. User asks a Question : Where is Mahur?
2. Automated Paraphrasing the questions ( managed by the LLM ) Q : Where is the location of a place called Mahur ?
3. Document Information Retrieval : We have used keyword search to search the document for retrieving the vital pieces of information for the question from the document. Alot of relevant information is extarcted out of the document which the LLM thinks MIGHT be useful to generate a response.
4. Response Generation : Now the information retireved from the document is used to answer the paraphrased question to generate a hyper-focused cpntext aware answer with data sources for the response generated by the LLM.
My approach to configuring ChatGPT for a religious scholar assistant role using Azure OpenAI Studio, prompt engineering, and Retrieval Augmented Generation (RAG) is well-structured and thorough. Here's a summary of the process:

### Prompt Engineering:
1. **Role Definition:**
   - Configuring ChatGPT to behave as a religious scholar assistant specifically for answering pilgrims' questions.

2. **Few-Shot Learning:**
   - Utilizing Few-Shot Learning techniques to train ChatGPT by providing examples of expected responses.
   - Example: Using the Bhagavad Gita as a few-shot learning example for instructive responses.

3. **Negative Prompts:**
   - Paying special attention to negative prompts to guide and restrict ChatGPT's responses, ensuring appropriate and respectful behaviour in conversations.

### Retrieval Augmented Generation (RAG):
1. **Document/Data Configuration:**
   - Utilizing Wikipedia articles on Mahur and two additional local news articles about Mahur in PDF format as the document/data for context-aware responses.

2. **User Question Processing:**
   - When a user asks a question (e.g., "Where is Mahur?"), an automated paraphrasing step is performed by the Language Model (LLM) to refine and structure the question. e.g. (Q : Where is the location of a place called Mahur ?)

3. **Document Information Retrieval:**
   - Employing keyword search to extract relevant information from the configured document.
   - Retrieving vital pieces of information that might be useful for generating a response.

4. **Response Generation:**
   - Utilizing the retrieved information to generate a hyper-focused, context-aware answer.
   - Including data sources in the response to provide transparency about the information's origin.

### Process Flow:
   - User question ➔ Automated paraphrasing ➔ Document information retrieval ➔ Response generation.

This approach ensures that ChatGPT, in its role as a religious scholar assistant, responds contextually and accurately by leveraging information from a well-defined document. The combination of prompt engineering and RAG enhances the model's understanding and responsiveness, contributing to a more tailored and reliable conversational experience for pilgrims seeking information.

# Red teaming: When does it fail?
In the context of a Temple Information QnA bot utilizing Language Model (LLM), similar challenges may be encountered:

1. **Limited Temple-specific Training Data:**
   - If the training data used to fine-tune the LLM model is inadequate in representing diverse temple-related queries, the bot may struggle to effectively respond to a broad range of user questions about temple information.

2. **Ambiguous Queries Pertaining to Temples:**
   - The bot may face difficulties with ambiguous queries related to temples, such as terms with multiple interpretations. For instance:
     - Query: "Puja"
     - Ambiguity: Does the user refer to a specific ritual or a place named Puja?

3. **Out-of-Domain Queries:**
   - If the LLM is primarily trained on a narrow set of temple-related documents or datasets, it may falter when presented with queries outside the realm of temple-related information.

4. **Unstructured Temple-related Data:**
   - When dealing with unstructured or noisy data related to temples, such as user-generated content with variations in language and spelling, the bot may struggle to provide accurate and relevant responses.

5. **Dynamic Temple Information:**
   - In cases where temple-related information changes rapidly, such as events, festivals, or renovations, the bot may offer outdated or incorrect responses if it doesn't have access to real-time updates.

6. **Incomplete Temple Context:**
   - If the training data lacks comprehensive coverage of various aspects of temple-related topics or lacks context, the bot may fail to generate accurate and contextually relevant responses for certain queries.

7. **Complex Temple-related Queries:**
   - The bot may encounter challenges in handling intricate queries that demand profound reasoning or synthesis of information from diverse sources related to temples.

8. **Sensitivity to Query Wording:**
   - Similar to RAG, the bot's performance might be sensitive to slight variations in how temple-related questions are phrased. Minor changes in wording could yield different responses.

Ensuring the effectiveness of the Temple Information QnA bot requires continuous monitoring, assessment, and refinement based on user interactions and evolving requirements. Fine-tuning the LLM with high-quality temple-specific data and addressing these challenges will enhance the bot's capability to deliver accurate and relevant information about temples.
