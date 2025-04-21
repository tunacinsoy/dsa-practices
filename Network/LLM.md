
> [!NOTE] What is Context Window?
> The _context window_ of a generative AI model refers to the maximum amount of information the model can consider at once when generating a response. It is usually measured in tokens (words and punctuation broken down into smaller chunks).
> ### Examples:
> 
> 1. **Short Context Window (e.g., 512 tokens)**
>     - Imagine you’re writing a story, but the model can only "remember" the last 512 tokens (roughly 300-400 words). As you keep adding text, the model starts to "forget" earlier parts of the story, which could lead to inconsistencies or a lack of coherence with the plot introduced earlier.
> 2. **Longer Context Window (e.g., 4096 tokens)**
>     - Now, suppose the model can handle 4096 tokens (about 2500-3000 words). In this case, it could keep track of more details from the start of a conversation, a complex story, or a long document, allowing it to generate content that maintains a consistent narrative or answers questions based on previous information.
> 
> ### Real-World Use:
> 
> - **Chat Applications**: In a long conversation with a chat model, a larger context window allows the model to recall earlier messages, making its responses relevant and coherent even after several exchanges.
> - **Document Summarization**: For summarizing a long article, a model with a longer context window can process more of the content at once, producing a more accurate summary.
> 
> A larger context window improves the model's ability to maintain focus and accuracy, but it also requires more computational power.


> [!NOTE] RAG vs Fine-Tuning
> RAG is generally superior for retrieving factual information that is not present in the
> LLM’s training data or is private. It allows you to dynamically integrate external knowledge without modifying the model’s weights. Fine-tuning, on the other hand, is more suitable for teaching the model specialized tasks or adapting it to a specific domain.

> [!NOTE] What is temperature parameter?
> The temperature parameter in Large Language Models (LLMs)  directly affects the variability and randomness of generated responses.  A lower LLM temperature value (close to 0) produces more deterministic and focused outputs,  ideal for tasks requiring factual accuracy, such as summarization or translation.
> ```python
> llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
> ```

