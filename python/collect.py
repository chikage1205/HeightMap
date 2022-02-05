import os
from bs4 import BeautifulSoup
import requests

images = [
    "Mountains/6.png",
    "Mountains/5.png",
    "Mountains/foothill1.png",
    "Mountains/range2.png",
    "Mountains/foothill2.png",
    "Mountains/range1.png",
    "Mountains/4.png",
    "Mountains/range3.png",
    "Mountains/range5.png",
    "Mountains/1.png",
    "Mountains/range4.png",
    "Mountains/foothill3.png",
    "Mountains/3.png",
    "Mountains/2.png",
    "Cells/Farm 1.png",
    "Cells/Cell 2.png",
    "Cells/Cell 1.png",
    "Cells/Cell 5.png",
    "Cells/Cell 3.png",
    "Cells/Cell 4.png",
    "Cells/Farm 2.png",
    "Dunes/Dunes1.png",
    "Dunes/andrewdune2.png",
    "Dunes/Dunes2.png",
    "Dunes/Dunes3.png",
    "Dunes/andrewdune1.png",
    "Dunes/Dunes4.png",
    "Dunes/Dunes5.png",
    "Dunes/andrewdune3.png",
    "DifferentMountains/2v2.png",
    "DifferentMountains/6.png",
    "DifferentMountains/5.png",
    "DifferentMountains/7v2.png",
    "DifferentMountains/7.png",
    "DifferentMountains/4.png",
    "DifferentMountains/4v2.png",
    "DifferentMountains/1.png",
    "DifferentMountains/3.png",
    "DifferentMountains/2.png",
    "goBrush/classic mountain 1.png",
    "goBrush/classic mountain 3.png.png",
    "goBrush/china mountain 1.png",
    "goBrush/sphere.png",
    "goBrush/crater.png",
    "goBrush/china mountain 2.png",
    "goBrush/plains cliff.png",
    "goBrush/smooth sphere.png",
    "goBrush/mesa.png",
    "goBrush/mountain 3.png",
    "goBrush/circle.png",
    "goBrush/volcano.png",
    "goBrush/mountain 2.png",
    "goBrush/mountain 1.png",
    "goBrush/sharp cliff.png",
    "goBrush/cliff.png",
    "goBrush/hills.png",
    "goBrush/classic mountain 2.png.png",
    "Geoglyph/Mountain 4.png",
    "Geoglyph/Mountain 2.png",
    "Geoglyph/Mountain 3.png",
    "Geoglyph/Mezozoic Test 1.png",
    "Geoglyph/Spine Ghost.png",
    "Geoglyph/Talus Spine.png",
    "Geoglyph/Mountain 1.png",
    "Geoglyph/Mezozoic Test 2.png",
    "Geoglyph/Talus Spine Mezozoic.png",
    "Rocks/Rocks 1.png",
    "Rocks/Circle rock 4.png",
    "Rocks/rocky99.png",
    "Rocks/Circle Rocks 1.png",
    "Rocks/Circle Rocks 3.png",
    "Rocks/Circle Rocks 2.png",
    "Rocks/Rocks 2.png",
    "Rocks/circlerock1.png",
    "Rocks/rocky9.png",
    "Cliff/Test.png",
    "Cliff/Cliff 5.png",
    "Cliff/zchasm1.png",
    "Cliff/Plateau 2.png",
    "Cliff/cliff 4.png",
    "Cliff/Cliff 6.png",
    "Cliff/Test2.png",
    "Cliff/cliff 3.png",
    "Cliff/Cliff 8.png",
    "Cliff/Cliff 7.png",
    "Cliff/Cliff.png",
    "Cliff/cliff1alt.png",
    "Cliff/Plateau 3.png",
    "Cliff/cliff 9.png",
    "Cliff/pointed cliff 1.png",
    "Cliff/Plateau.png",
    "Cliff/Plateau 4.png",
    "Cliff/zchasm.png",
    "Cliff/cliff 2.png",
    "Cliff/cliff 1.png",
    "RealWorldData/Fjord1.png",
    "RealWorldData/Fjord3.png",
    "RealWorldData/test2.png",
    "RealWorldData/test3.png",
    "RealWorldData/test4.png",
    "RealWorldData/test6.png",
    "RealWorldData/test5.png",
    "RealWorldData/Fjord2.png",
    "RealWorldData/test7.png",
    "RealWorldData/test.png",
    "ChinaMountains/China Mountain 2.png",
    "ChinaMountains/China Mountain 4.png",
    "ChinaMountains/China Mountain 5.png",
    "ChinaMountains/China Mountain 3.png",
    "ChinaMountains/China Mountain 1.png",
    "Misc/Circle.png",
    "Misc/B601C3.png",
    "Misc/Shape 3.png",
    "Misc/Biomes.png",
    "Misc/B601C1.png",
    "Misc/A601B3.png",
    "Misc/A601B2.png",
    "Misc/B601C2.png",
    "Misc/Shapes.png",
    "Misc/Materials 1.png",
    "Misc/Shape 2.png",
    "Misc/A601B1.png",
    "Misc/Plains 1.png",
    "DesertRock/Desert Rocks 5.png",
    "DesertRock/Desert Rock 1.png",
    "DesertRock/Desert Rock 3.png",
    "DesertRock/Desert Rock 2.png",
    "DesertRock/Desert Rock 4.png",
    "WPmade/Pixel_1.png",
    "WPmade/Me_Mountain_2.png",
    "WPmade/Me_7.png",
    "WPmade/Me_2.png",
    "WPmade/Me_5.png",
    "WPmade/Me_1.png",
    "WPmade/Me_6.png",
    "WPmade/Me_4.png",
    "WPmade/Me_3.png",
    "WPmade/Me_Mountain.png",
    "WPmade/Pixel_Mountain.png",
    "WPmade/Me_Mountain_3.png",
    "WPmade/Me_Mountain_4.png",
    "WPmade/Pixel_2.png"
]

site_url = "https://www.buildersrefuge.com/heightmap/"
src_min = "images/min/"
src_max = "images/max/"

def download_image(url, timeout = 10):
    response = requests.get(url, allow_redirects=False, timeout=timeout)
    if response.status_code != 200:
        e = Exception("HTTP status: " + response.status_code)
        raise e

    content_type = response.headers["content-type"]
    if 'image' not in content_type:
        e = Exception("Content-Type: " + content_type)
        raise e

    return response.content

def save_image(filename, image):
    dirname = os.path.dirname(__file__)+"/"+"/".join(filename.split("/")[:-1])
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    with open(filename, "wb") as fout:
        fout.write(image)

for image in images:
    min_url = src_min+image
    max_url = src_max+image

    min_image = download_image(site_url+min_url)
    max_image = download_image(site_url+max_url)

    save_image(min_url, min_image)
    save_image(max_url, max_image)


