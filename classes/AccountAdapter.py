import classes.AccountFactory


class AccountAdapter:

    def createFromJSON(type,jsonObject):
        if type == "Patient":
            patient = classes.AccountFactory.AccountFactory.get_account("Patient")
            patient.last_name    = jsonObject['last_name'    ]
            patient.first_name   = jsonObject['first_name'   ]
            patient.email        = jsonObject['email'        ]
            patient.password     = jsonObject['password'     ]
            patient.card_number  = jsonObject['card_number'  ]
            patient.birth_day    = jsonObject['birth_day'    ]
            patient.gender       = jsonObject['gender'       ]
            patient.phone_number = jsonObject['phone_number' ]
            patient.address      = jsonObject['address'      ]
            return patient
        elif type == "Doctor":
            doctor = classes.AccountFactory.AccountFactory.get_account("Doctor")
            doctor.last_name     = jsonObject['last_name'     ]
            doctor.first_name    = jsonObject['first_name'    ]
            doctor.email         = jsonObject["email"         ]
            doctor.password      = jsonObject["password"      ]
            doctor.permit_number = jsonObject["permit_number" ]
            doctor.location      = jsonObject["location"      ]
            doctor.speciality     = jsonObject["speciality"     ]
            return doctor
        elif type == "Nurse":
            nurse = classes.AccountFactory.AccountFactory.get_account("Nurse")
            nurse.last_name  = jsonObject['last_name'  ]
            nurse.first_name = jsonObject['first_name' ]
            nurse.email      = jsonObject["email"      ]
            nurse.password   = jsonObject["password"   ]
            nurse.access_id  = jsonObject["access_id"  ]
            return nurse
    
    def updateFromJSON(type,account,jsonObject):
        if type == "Doctor":
            account.last_name     = jsonObject['last_name'     ]
            account.first_name    = jsonObject['first_name'    ]
            account.email         = jsonObject["email"         ]
            account.password      = jsonObject["password"      ]
            account.permit_number = jsonObject["permit_number" ]
            account.location      = jsonObject["location"      ]
            account.specialty     = jsonObject["speciality"     ]
            return account
        elif type == "Patient":
            account.last_name    = jsonObject['last_name'    ]
            account.first_name   = jsonObject['first_name'   ]
            account.email        = jsonObject["email"        ]
            account.password     = jsonObject["password"     ]
            account.card_number  = jsonObject['card_number'  ]
            account.birth_day    = jsonObject['birth_day'    ]
            account.gender       = jsonObject['gender'       ]
            account.phone_number = jsonObject['phone_number' ]
            account.address      = jsonObject['address'      ]
            return account
        elif type == "Nurse":
            account.last_name  = jsonObject['last_name'  ]
            account.first_name = jsonObject['first_name' ]
            account.email      = jsonObject["email"      ]
            account.password   = jsonObject["password"   ]
            account.access_id  = jsonObject["access_id"  ]
            return account


