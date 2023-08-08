my_resume = { "name":"Libin",
              "email":"libin3636@gmail.com",
              "mobile-no":8870667205,
              "soft_skills":["Time Management","Teamwork","Problem Solving"],
              "hard_skills":["Degree","Software Knowledge","Programming Knowledeg"],
              "education_qualification":[{"level":"BCA",
                                          "ins_name":"Scott College",
                                          "passedout_year":2023,
                                          "mark_percentage":70},
                                         {"level":"HSC",
                                          "ins_name":"GHSS Ammandivilai",
                                          "passedout_year":2020,
                                          "mark_percentage":62},
                                         {"level":"SSLC",
                                          "ins_name":"Carmel School",
                                          "passedout_year":2018,
                                          "mark_percentage":81},
                                         ],
              "projects":[{"proj_name":"Car Rental portel","language_used":["HTML","CSS","Java Script","Python","MySql"]},
                          {"proj_name":"Online shopping website","language_used":["HTML","CSS","Java Script","Python","MySql"]}
                          ],
              "experience":[{"company_name":"Capestar","experience":1.4,"role":"manager"},
                            {"company_name":"Amazon","experience":5,"role":"Developer"}
                            ],
              "hobbies":["Bike Riding","volley ball","Running"],
              "personal_details":{ "father_name":"Lingathurai",
                                   "father_occupation":"Cooli",
                                   "languages_known":["Tamil","English"],
                                   "dob":"16/06/2003",
                                   "gender":"Mail",
                                   "martial_status":"Unmaried",
                                   "address":{"door_no":"25/168-11",
                                              "street":"Thivandakottai",
                                              "city":"Ammandivilai",
                                              "pincode":"629204"}
                                },
               "declaration":"I hereby declare that the details and information given above are complete and true to the best of my knowledge"
            }

print (my_resume)

print (my_resume["name"])

print (my_resume["mobile-no"])

print (my_resume["soft_skills"][0])

print (my_resume["education_qualification"][2])

print (my_resume["personal_details"]["father_name"])

print (my_resume["personal_details"]["address"])

print (my_resume["personal_details"]["address"]["pincode"])