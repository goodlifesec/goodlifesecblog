import os
import re
import shutil

# Paths (using raw strings to hand windows backslashes correctly)
posts_dir = r"C:\Users\Jerry\Documents\GoodLifeSec\goodlifesecblog\content\posts"
print(posts_dir)
attachments_dir = r"C:\Users\Jerry\Documents\Obsidian_Vault1\Blog\Posts\attachements"
print(attachments_dir)
static_images_dir = r"C:\Users\Jerry\Documents\GoodLifeSec\goodlifesecblog\static\images"
print(static_images_dir)

# 1. Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)

        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()

        # 2. Find all image links in the format ![Image Description](/images/Pasted%20image%20...%20.png) with image extensions
        images = re.findall(r'!\[\[([^]]*\.(?:webp|png|gif|jpg))\]\]', content)

        # 3. Replace image links and ensure URLs are correctly formatted
        for image in images:
            # Prepare the Markdown-compatable link with %20 replacing spaces
            markdown_image = f"[Image Description](/images/{image.replace(' ', '%20')})"
            # remove the "!" from before [Image Descriptio]
            content = content.replace(f"[[{image}]]", markdown_image)

            # 4. Copy the image to the Hugo static/images directory if it exists
            image_source = os.path.join(attachments_dir, image)
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)

        # 5. Write the updated content back to the markdown file
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

print("Markdown files processed and images copied successfully.")