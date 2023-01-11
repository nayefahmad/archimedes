# The Archimedes Project 

## Architecture specifications

- Database 
  - sqlite/postgres/duckDB database hosted on a server 
- CI/CD 
  - Github actions to run tests, and to update db regularly? 
- Testing 
  - pytest 
  - coverage report in repo 
- Repo structure 
  - `models.py` for ORM classes, `pipelines.py` for data access and pipelines
    - OR: use `data_access/` dir? 
  - `data/` for example csv data 
  - `archimedes/` for analysis code 
    - `archimedes/forecasting/`
    - `archimedes/plotting/`
    - `archimedes/preprocessing/`
  - `test/` for tests 
    - `test_archimedes/` for unit tests 
    - `test_integration/` for integration tests? 


### Review of Component Monitoring project architecture specifications 

- Code and containers on GitLab 
- Server has postgresql DB on port 5433. URL: `jdbc:postgresql://<address>:5433/cm_db`


## Analysis/modeling specifications 
- STL decomposition 
- Comparison with forecast 
- Outlier detection 
- Correlation with walking data? 


## References 

- Google Cloud run 
  - [Google Cloud Run - Deploy a Python service to Cloud Run](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service)
- Cloud DBs: 
  - [MongoDB Atlas Cloud DB](https://www.mongodb.com/atlas/database)
  - [bit.io](https://docs.bit.io/docs/connecting-via-pandas-1)


## Other stuff 

```mermaid
  graph TD;
      A-->B;
      A-->C;
      B-->D;
      C-->D;
```

