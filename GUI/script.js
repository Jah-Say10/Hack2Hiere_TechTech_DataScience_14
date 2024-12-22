window.onload = (event) =>
{
    let validerBtn = document.getElementById("valider")
    
    validerBtn.addEventListener("click", () => 
    {
        // Age
        let age = document.getElementById("age").value

        // Sex
        let sex_list = document.getElementsByName("sex")
        let sex = ""
        for (i = 0; i < sex_list.length; i++)
        {
            if (sex_list[i].checked)
            {
                sex = sex_list[i].value
                break
            }
        }

        // Job
        let job = document.getElementById("job").value

        // Housing
        let housing_list = document.getElementsByName("housing")
        let housing = ""
        for (i = 0; i < housing_list.length; i++)
        {
            if (housing_list[i].checked)
            {
                housing = housing_list[i].value
                break
            }
        }

        // Saving accounts
        let saving_accounts_list = document.getElementsByName("saving_accounts")
        let saving_accounts = ""
        for (i = 0; i < saving_accounts_list.length; i++)
        {
            if (saving_accounts_list[i].checked)
            {
                saving_accounts = saving_accounts_list[i].value
                break
            }
        }

        // Checking account
        let checking_account_list = document.getElementsByName("checking_account")
        let checking_account = ""
        for (i = 0; i < checking_account_list.length; i++)
        {
            if (checking_account_list[i].checked)
            {
                checking_account = checking_account_list[i].value
                break
            }
        }

        // Credit amount
        let credit_amount = document.getElementById("credit_amount").value

        // Duration
        let duration = document.getElementById("duration").value

        // Purpose
        let purpose_list = document.getElementsByName("purpose")
        let purpose = ""
        for (i = 0; i < purpose_list.length; i++)
        {
            if (purpose_list[i].checked)
            {
                purpose = purpose_list[i].value
                break
            }
        }

        data = age + "," + sex + "," + job + "," + housing + "," + saving_accounts + "," + checking_account + "," + credit_amount + "," + duration + "," + purpose
        
        let url = "http://localhost:8000/predict/"+data

        $.ajax({
            url: url,
            method: 'GET',
            success: function(response) {
                // Handle the API response here
                console.log(response);

                if(response["good"] <= 0.5)
                {
                    document.getElementById("text").innerHTML = "Il y a un grand nombre de risques liés à l'octroi de crédit à cette personne, il est donc important de faire attention avant de contracter un prêt.<br> Probabilite paiement: " + response["good"] + "<br> Probabilite de defaut:" + response["bad"]
                }
                else
                {
                    document.getElementById("text").innerHTML = "Étant donné que les risques liés à l'octroi de crédit à cette personne sont faibles, vous pouvez accorder le prêt.<br> Probabilite paiement: " + response["good"] + "<br> Probabilite de defaut:" + response["bad"]

                }
            },
            error: function(xhr, status, error) {
                // Handle errors here
                console.error(status, error);
            }
        });
    })
};

age + "," + sex + "," + job + "," + housing + "," + saving_accounts + "," + checking_account + "," + credit_amount + "," + duration + "," + purpose
"32,male,0,rent,rich,little,10000,10,business"