"use client"
import {Button, Label, Textarea, TextInput} from "flowbite-react";
import httpClient from "@/services/httpClient";
import {useState} from "react";
import {useRouter} from "next/router";

export default function Submit() {
    const [isLoading, setIsLoading] = useState(false)
    const router = useRouter()
    const handleSubmit = async (e) => {
        e.preventDefault();

        const formData = new FormData(e.target);
        const formValues = {};

        for (let [key, value] of formData.entries()) {
            formValues[key] = value;
        }
        setIsLoading(true)
        await httpClient.post('requests/submit', formValues)
        setIsLoading(false)
        alert('demande a bien été envoyé')
        router.push('/request')
    };
    return (
        <>
            <div className="flex justify-center w-full">
                <div className="w-1/3">
                    <h2 className={"my-4"}>Soumettre votre demande</h2>
                    <form className="flex max-w-md flex-col gap-4" onSubmit={handleSubmit}>
                        <div>
                            <div className="mb-2 block">
                                <Label htmlFor="text" value="Contenu de la demande"/>
                            </div>
                            <Textarea id="text" name="text"
                                      placeholder="Soumettre votre demande en respectant les signes suivants, comment vous appelez, le montant du pret demandé, l'adresse du logement, la description de la propriété."
                                      required rows={6}/>
                        </div>

                        <Button type="submit" isProcessing={isLoading}>Submit</Button>
                    </form>
                </div>
            </div>
        </>
    )
}