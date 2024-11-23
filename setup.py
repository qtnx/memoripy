from setuptools import setup, find_packages

setup(
    name="memoripy",
    version="0.1.0",
    author="Khazar Ayaz",
    author_email="khazar.ayaz@personnoai.com",
    description="Memoripy provides context-aware memory management with support for OpenAI and Ollama APIs, offering structured short-term and long-term memory storage for interactive applications.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/caspianmoon/memoripy",
    packages=find_packages(),
    install_requires=[
        "aiohappyeyeballs==2.4.3",
        "aiohttp==3.10.10",
        "aiosignal==1.3.1",
        "annotated-types==0.7.0",
        "anyio==4.6.2.post1",
        "attrs==24.2.0",
        "certifi==2024.8.30",
        "charset-normalizer==3.4.0",
        "distro==1.9.0",
        "faiss-cpu==1.8.0.post1",
        "frozenlist==1.5.0",
        "h11==0.14.0",
        "httpcore==1.0.6",
        "httpx==0.27.2",
        "idna==3.10",
        "jiter==0.7.0",
        "joblib==1.4.2",
        "jsonpatch==1.33",
        "jsonpointer==3.0.0",
        "langchain==0.3.7",
        "langchain-core==0.3.15",
        "langchain-ollama==0.2.0",
        "langchain-openai==0.2.5",
        "langchain-text-splitters==0.3.2",
        "langsmith==0.1.139",
        "multidict==6.1.0",
        "networkx==3.4.2",
        "numpy==1.26.4",
        "ollama==0.3.3",
        "openai==1.54.0",
        "orjson==3.10.11",
        "packaging==24.1",
        "propcache==0.2.0",
        "pydantic==2.9.2",
        "pydantic_core==2.23.4",
        "PyYAML==6.0.2",
        "regex==2024.9.11",
        "requests==2.32.3",
        "requests-toolbelt==1.0.0",
        "scikit-learn==1.5.2",
        "scipy==1.14.1",
        "setuptools==75.3.0",
        "sniffio==1.3.1",
        "SQLAlchemy==2.0.36",
        "tenacity==8.5.0",
        "threadpoolctl==3.5.0",
        "tiktoken>=0.7.0,<0.8.0",
        "tqdm==4.66.6",
        "typing_extensions==4.12.2",
        "urllib3==2.2.3",
        "yarl==1.17.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
