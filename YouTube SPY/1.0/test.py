from googleapiclient.discovery import build
import urllib.parse as p

# 你的API密钥
api_key = "AIzaSyBFeEuAPLSjwSBcIo4Yqu0yAaSUK63gQ2U"  //请在这里更换为你的秘钥信息，该秘钥随时失效

def get_video_categories():
    # 创建YouTube的API客户端
    youtube = build('youtube', 'v3', developerKey=api_key)

    # 调用API接口获取所有的视频分类
    request = youtube.videoCategories().list(
        part="snippet",
        regionCode="US"
    )
    response = request.execute()

    # 将分类ID和分类名称保存在一个字典中
    categories = {}
    for item in response["items"]:
        categories[item["id"]] = item["snippet"]["title"]
    
    return categories

def get_video_info(video_url, categories):
    # 从URL中解析出视频ID
    url_data = p.urlparse(video_url)
    query = p.parse_qs(url_data.query)
    video_id = query["v"][0]

    # 创建YouTube的API客户端
    youtube = build('youtube', 'v3', developerKey=api_key)

    # 调用API接口获取视频信息
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=video_id
    )
    response = request.execute()

    # 从API的返回结果中提取出视频的信息
    items = response.get("items")
    if items:
        item = items[0]
        snippet = item["snippet"]
        return {
            "title": snippet["title"],
            "description": snippet["description"],
            "tags": snippet["tags"],
            "thumbnail": snippet["thumbnails"]["default"]["url"],
            "publishedAt": snippet["publishedAt"],
            "category": categories.get(snippet["categoryId"], "Unknown"),
        }
    else:
        return None

def main():
    categories = get_video_categories()
    while True:
        video_url = input("请输入YouTube视频的地址，或者输入'q'退出：")
        if video_url.lower() == 'q':
            break
        info = get_video_info(video_url, categories)
        if info:
            print("视频标题：", info["title"])
            print("视频描述：", info["description"])
            print("视频标签：", ", ".join(info["tags"]))
            print("视频缩略图：", info["thumbnail"])
            print("发布时间：", info["publishedAt"])
            print("发布分类：", info["category"])
        else:
            print("无法获取视频信息。")

if __name__ == "__main__":
    main()

input("Press Enter to exit...")
