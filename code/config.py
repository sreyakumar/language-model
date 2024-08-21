toolConfig = {
  "tools": [
      {
      "toolSpec": {
          "name": "one_doc_retrieval",
          "description": "Retrieve one document from docDB. Only to be used if the prompt expresses certainty that one document should be accessed.",
          "inputSchema": {
              "json": {
                  "type": "object",
                  "properties": {
                      "filter": {
                          "type": "string",
                          "description": "A MongoDB query to pass to the function"
                      }
                  },
                  "required": ["filter"]
              }
          }
      }
      },
      {
      "toolSpec": {
          "name": "multi_doc_retrieval",
          "description": "Retrieve multiple documents from docDB. Used in cases where multiple documents need to be retrieved",
          "inputSchema": {
              "json": {
                  "type": "object",
                  "properties": {
                      "filter": {
                          "type": "string",
                          "description": "A MongoDB query to pass to the function"
                      }
                  },
                  "required": ["filter"]
              }
          }
      }
      }
  ]
}


