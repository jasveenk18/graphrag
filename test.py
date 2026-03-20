from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    "neo4j+s://513a2397.databases.neo4j.io",
    auth=("neo4j", "i8s6xa2n7d19ck8YR6dWbhlEJCKeG0Ttsm2ADZnmagw ")
)

with driver.session() as session:
    print(session.run("RETURN 1").single())

driver.close()