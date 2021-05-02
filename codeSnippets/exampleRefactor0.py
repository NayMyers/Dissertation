results = results[0]
results = results.tolist()
jsonResults = json.dumps(results)

return{
"results" : jsonResults,
}
