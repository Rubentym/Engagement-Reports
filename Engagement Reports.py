def generate_engagement_report(data):
    # Generate engagement report (e.g., average engagement rate, top posts)
    avg_engagement = sum([post["engagement"] for post in data.get("posts", [])]) / len(data.get("posts", []))
    top_posts = sorted(data.get("posts", []), key=lambda post: post["engagement"], reverse=True)[:5]
    return avg_engagement, top_posts

avg_engagement, top_posts = generate_engagement_report(social_media_data)
print("Average Engagement Rate:", avg_engagement)
print("Top Posts:")
for post in top_posts:
    print(post)
