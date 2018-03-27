import polygon_to_points
import get_village_points
import GSV_loader
import argparse
import os

keys = [
        "AIzaSyA6zubCrlHlZWT2joBJGJLJiM6vdYr6oEM",
        "AIzaSyCDGjA_AHTLlH1oknEXQo7REWZTROa7BiE",
        "AIzaSyA5mWEWwtPokDUv2lNulBQVUlJ72kdtSMQ",
        "AIzaSyCJkRo1CosMif2G6nzT1_9zeI6BJaTUJTA",
        "AIzaSyCDGjA_AHTLlH1oknEXQo7REWZTROa7BiE",
        "AIzaSyDlLnmGz8Gz2G-y1zC7dn5GJRJC3t4tbP4",
        "AIzaSyDdcR18EiXRHIGBUXN2tAaC63ktfTEHN3g",
        "AIzaSyCbs_iKDVssx0ngHqjVaGlMl12bvP-axj0",
        "AIzaSyC19LaqI24SRjvywXX34hLIfWKW07NHnGI",
        "AIzaSyCI_8p7rmObwr7uJKGwoo3oPkeBVuKHIzw",
        "AIzaSyAk5pMGnr4hv8X4ph1guOqAgNH2PUB-j14",
        "AIzaSyAIPElNOZ7sS83a-3VOe-Mw9_wUiF9sMpo",
        "AIzaSyBAqGnlTnwQnVENrVSyHWBh1AwhIZcP5Oo",
        "AIzaSyA5mWEWwtPokDUv2lNulBQVUlJ72kdtSMQ",
        "AIzaSyAXEU3aHmEHuBa80yOSrUyneL9OIWogE9Y",
        "AIzaSyDm1VQNO4-RtmNlUYYFDeGarFpIVAnn9cc",
        "AIzaSyAOmGuWFhrhDQK-8c44Ln2wBATByS-Qv-Q",
        "AIzaSyAiRjkmZz23X7IQ6KLoqfgbvlBio6mGHl4",
        "AIzaSyBiuww1q7s6lIEG4v5yauaeiw-z5YNoN60"
       ]

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
      '--province',
      type=str,
      help='province/city name (จังหวัด)',
      required=True
    )
    parser.add_argument(
      '--district',
      type=str,
      help='district name (Amphoe อำเภอ)',
      required=True
    )
    parser.add_argument(
      '--subdist',
      type=str,
      help='sub-district name (Tambon, ตำบล)',
      required=True
    )
    parser.add_argument(
      '--village',
      type=str,
      help='village name (หมู่บ้าน)',
      required=True
    )

    FLAGS, unparsed = parser.parse_known_args()

    province = FLAGS.province.decode('utf8')
    district = FLAGS.district.decode('utf8') 
    subdist = FLAGS.subdist.decode('utf8')
    village = FLAGS.village.decode('utf8')

    points = polygon_to_points.run(province, district, subdist)
    if(points != 'error'):
      vill_points = get_village_points.run(province, district, subdist, village, points, keys[0])
      path = os.path.join('../GSV',province, district, subdist, village,'original')
      GSV_loader.run(vill_points, path, keys)