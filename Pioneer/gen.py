import json

baseJson = {
	"description": '''Coinhub Pioneer User.''',
	"background_color": "ffffff",
	"external_url": "https://coinhub.org",
	"image": "https://coinhublab.github.io/Pioneer/NFT.png",
	"name": "Pioneer User NFT ",
	"animation_url": ""
}


def genJson(id):
	item = baseJson
	rawName = item["name"]
	with open("%d.json" % id, "w") as fJson:
		item["name"] += "#%03d" % id
		fJson.write(json.dumps(item, ensure_ascii=False))
	item["name"] = rawName
		
if __name__ == "__main__":
	print("hello")
	print(baseJson)
	for i in range(0,634):
		genJson(i)
