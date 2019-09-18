import subprocess as sb
import json

hubs = open ('/Users/tim/Google Drive File Stream/My Drive/Colab Notebooks/battery/hubs').readlines ()

from_battery = ["""
5a8eef6b0446f007bd4eff0d
 0c88e911-f132-4581-822a-a95f8d92f664_6
 107a1d4e-6d34-43b7-a65e-564b2f3eed47_9
 2e28f672-f35c-49eb-9dc2-6325c610f97e_2
 63c7d81e-3dad-4000-b6cd-d62ce7a5a90f_14
 685c2f30-26ce-46d1-92c3-4a1dc7d3bf5b_15
 93a84422-3f35-417a-ab81-769ee1aab19b_12
 93a84422-3f35-417a-ab81-769ee1aab19b_18
 93a84422-3f35-417a-ab81-769ee1aab19b_7
 97c4123a-465e-44b2-82f1-e5eae87efd93_3
 b0a44ea1-0299-4098-8223-eaa3ac07b33c_19
 c2c7ac09-7efd-4ba3-bc6e-211189270855_5
 c30a517c-24ef-42d5-9eb8-b93eaf0dfe69_4
 e8b5c5e0-0f83-4650-baf8-9e4fd9654535_13
 """,
 """
 5a992175bbda2e2cc46b2d23
 6968db56-d0a0-45de-bff3-996870372659_3
 c12bfb26-3109-4008-b035-0db92631598c_4
 """,
 """
 5a992264bbda2e2cc46b2f21
 2349c46e-0d4a-424e-8587-8313cae2a40c_7
 89acb87e-57fe-49ae-ab7a-d86f43706d81_9
 9e2086c5-9785-4e44-8072-a42afd8c02db_13
 9e2086c5-9785-4e44-8072-a42afd8c02db_8
 a7086c93-b721-4bb4-b44f-4865b459615f_3
 b8357a9c-f26f-4caf-803d-5913f4ddd964_10
 bbc98359-6384-452a-8818-80ce4a88302b_5
 bff035cb-16a2-447e-8995-ed20a98a352d_6
 e230c038-3e35-4fa0-bdb1-b4eaf63cd2a0_15
 """,
 """
 5aa147d1bbda2e2cc46bb73e
 062ff494-e78b-424b-a610-8c14d3733cd8_7
 240dc142-68a2-4430-8c4c-8a53a0233f41_3
 2c26f7c8-3528-43bc-ab87-f76b520e7e41_5
 6b301afd-8952-43f9-869e-4265acb3bca4_14
 6f1d580e-477d-48ba-9012-3ba3579f4518_4
 8637651f-472d-4505-afe1-66e040525e81_13
 c9a4d268-d69f-4103-9566-41ccbc6c0d63_6
 """,
 """
 5af42949c7fe05062907921e
 0f5c8132-87e4-4c66-b40d-c9865160126a_7
 340523d6-e133-4409-97ea-a9349426065c_4
 3eb23758-8630-4855-b774-ea2a626f3ce8_9
 60e700d1-2ae1-4df2-8996-575f687d5b8d_6
 61beee9a-2581-47b8-9b72-e19c457284db_8
 98be8e9e-a1e8-49d5-994f-3e8a4bac6ebb_3
 ae29be44-deb9-496a-9785-bef150daaf71_10
 e4831450-c06a-43d8-974d-2fe68a4ca5e7_5
 f83df848-1f8c-4b8b-8e9a-993cfe1a59df_2
 """,
 """
 5b1e3f62c7fe056c961f0639
 46a23c05-2275-4dba-a1ca-fb9655cbb1a2_4
 """,
 """
 5b1fb903c7fe056c9620741b
 0207097b-ffed-4ec3-bac4-9a7ea3a49d44_3
 0695abb8-9e9d-4a04-8171-24e18a30e817_7
 2d558ecd-9cf6-4367-beb5-6666b3bc75eb_23
 2d558ecd-9cf6-4367-beb5-6666b3bc75eb_24
 50469bce-71ef-4a19-ac6b-e4dc782004ee_6
 67fc98d6-e769-4ea1-b7c2-7b74c5720cea_4
 83938043-e29e-4521-8f49-5bbf05ffbc9a_18
 889785c4-a1f4-499f-b4fd-47806b692a22_8
 8a347eec-b71f-4083-a5cd-73f01ee95994_19
 96cce860-08d3-491d-af5d-5ba026ed931c_17
 f41c1696-cb36-4958-8f30-7d3450bcb7fa_5
 """,
 """
 5b225850c7fe056c9624783c
 0f181d71-ed63-47f0-9cda-6a9eca433610_18
 18514e09-2f98-4ac6-af6e-b8ded6e71d3c_20
 285fefb6-156e-401d-9c17-eba8756690f0_8
 5633308c-df68-477e-bd57-9d85853b6398_5
 57bc8f68-fd59-46a2-9a52-f1ab3b2d810f_19
 86667dd1-7468-4539-8269-48b93ff479c0_16
 9122ad6c-861f-46ea-8b7d-a6705ac129a9_21
 ac8fc2c8-aae0-40e9-9eb1-0a64c08122f3_4
 c3cac075-2a5a-46f0-83a9-c9f0dd868aa8_6
 e56df0fb-8b06-474a-9167-818a523572d8_7
 """,
 """
 5d08a07fc7fe05618c374ab5
 28bb90f9-31f8-4009-8852-752f2c1b854e_10
 28bb90f9-31f8-4009-8852-752f2c1b854e_7
 408122a7-94aa-4e44-a8ec-74979e51ea2e_3
 67e23193-1c7b-4ca5-842d-65fdaf8036a2_10
 6db323fa-affd-4bb9-9b04-baecd81cb054_13
 6db323fa-affd-4bb9-9b04-baecd81cb054_8
 77a5492c-acc2-4b92-a875-e44fef771a0e_4
 7dcf27b8-2552-4313-9313-307eb7e5f267_2
 cca3eaa0-610b-45f3-954b-d9a740f35ab8_11
 cca3eaa0-610b-45f3-954b-d9a740f35ab8_8
 d0203a38-c4ec-45b7-819f-071ff53fd8cb_6
 ebe91779-b3b0-41b9-a5b6-2f260766111d_10
 ebe91779-b3b0-41b9-a5b6-2f260766111d_7
 edd07d1d-7ce4-4d2f-a2ae-13fa0ccdb4c2_5
 """,
 """
 5d25b901c7fe05081ab12ce2
 1daee14e-bcf3-494b-b825-431681153b00_9
 5f7f8471-1ee4-4e7b-812d-2b9c4b84f645_6
 6a366078-7789-49a6-aef6-65931919ef10_8
 81e38c85-decb-4691-be52-44f88a8d99c4_3
 8d1fc555-ecd0-4902-9771-a5c4ca44b0d1_2
 b4957289-ec2e-4c4f-96e9-107a997e64ff_4
 c8c399da-fb19-4c69-b564-d819f8cda14f_5
 ffc51842-cd4f-4ead-893a-9b489740839b_7
 """,
 """
 5d3ea83ac7fe0554e22ae04c
 05d9e859-ebd8-486e-a70c-7b0546101237_9
 3cd133cd-8b66-4997-8483-35749c4e0f7e_14
 4b93100d-b93a-419c-a194-15d78859c639_4
 6801c5d5-0284-4991-a0ab-bcc8d40e66f7_10
 6d585327-1bbf-4bd3-88af-1b76b52c3a34_3
 816edb94-69ff-46d0-b5d4-bf657b184351_8
 88d865d8-1cdf-4756-af1a-5f87e898c497_2
 a6d2364d-482d-4684-978d-04030769cf8a_7
 c58c12d1-f673-49d3-8e4e-2e75f01f2eae_5
 c5a2ac23-67ba-4c23-bee0-4840cc35d809_6
 f35f79d2-28ee-47bd-a956-1aaf1095eb27_13
"""]


def devs_for_hub_from_live (h):
    #for h in hubs: #["5a8eef6b0446f007bd4eff0d"]: #hubs:
    devs = []
    h = h.strip ()
    js = sb.check_output ('curl --header "Content-Type: application/json" https://homeinstead.anthropos.io/PumpHouse/rest/v1/iot/users/{}/residences'.format (h), shell=True)
    #print (js)
    cust = json.loads (js)

    print (h, cust['residence'][0]['fn'])
    #print (cust['residence'][0]['devices'])
    for l in cust['residence'][0]['locations']:
        #print (l.keys())
        for slot in l['deviceSlots']:
            for d in slot['devices']:
                print ("physical", d['uuid'], d['model'])
                #devs.append (d['uuid'])
            if all (('power' not in slot ['deviceType'], 'pressure' not in slot ['deviceType'])):   # ignore power meters for battery stuff
                print (slot['uuid'], slot ['deviceType'])
                devs.append (slot['uuid'])
    return cust ['residence'][0]['fn'], devs
#

class hub ():
    def __init__ (self, str):
        vals = str.split ()
        self.id = vals [0]
        self.devs = [x.split ('_')[0] for x in vals [1:]]
        #print (self.devs)

from_live = {}
names = {}

for h in hubs:
    names [h.strip ()], from_live [h.strip()] = devs_for_hub_from_live (h.strip ())

from_excel = {}
for h_str in from_battery:
    h = h_str.split ()[0]
    #print ("hh", h)
    from_excel [h] = hub (h_str)


print (from_excel.keys())
print (from_live.keys())

print (from_excel.keys () == from_excel.keys())

for k in from_excel.keys ():
    print ("\n\n", names[k], k)
    #print (from_excel [k].devs, from_live[k])
    print ("common devices", len (set (from_excel[k].devs).intersection (set (from_live[k]))))
    print ("historical, not current", len (set (from_excel [k].devs).difference (set (from_live[k]))))
    print ("current not historical", len (set (from_live [k]).difference (set (from_excel[k].devs))))


"""
#print (devs)
#print (x.devs)
"""
