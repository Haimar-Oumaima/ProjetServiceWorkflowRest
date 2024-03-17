"use client"
import {Button, Label, Textarea, TextInput} from "flowbite-react";
import httpClient from "@/services/httpClient";

export default function Submit() {
    const handleSubmit = async (e) => {
        e.preventDefault();

        const formData = new FormData(e.target);
        const formValues = {};

        for (let [key, value] of formData.entries()) {
            formValues[key] = value;
        }
        const payload = {
            nom: formValues.nom,
            prenom: formValues.prenom,
            adresse: formValues.adresse,
            num_tel: formValues.telephone,
            email: formValues.email,
            password: formValues.password,
        }
        console.log("payload", payload)
        const result = await httpClient.post('login_register/register', payload)
        console.log(result);
        // Vous pouvez envoyer les données à votre backend ou effectuer
    };
    return (
        <>
            <h2>Soumettre votre demande</h2>
            <form className="flex max-w-md flex-col gap-4" onSubmit={handleSubmit}>

                <div>
                    <div className="mb-2 block">
                        <Label htmlFor="demande" value="Contenu de la demande"/>
                    </div>
                    <Textarea id="demande" name="demande"
                              placeholder="Soumettre votre demande en respectant les signes suivants, comment vous appelez, le montant du pret demandé, l'adresse du logement, la description de la propriété."
                              required rows={6}/>
                </div>

                <Button type="submit">Submit</Button>
            </form>

        </>
    )
}