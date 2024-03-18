"use client"

import {Button, Label, Textarea, TextInput} from "flowbite-react";
import httpClient from "@/services/httpClient";
import {useRouter} from "next/router";

export default function Register() {
    const router = useRouter()
    const handleSubmit = async (e) => {
        e.preventDefault();

        const formData = new FormData(e.target);
        const formValues = {};

        for (let [key, value] of formData.entries()) {
            formValues[key] = value;
        }

        // Check telephone format
        if (!/^\d{10}$/.test(formValues.telephone)) {
            alert("Please enter a valid 10-digit telephone number.");
            return;
        }

        // Check email format
        if (!/\S+@\S+\.\S+/.test(formValues.email)) {
            alert("Please enter a valid email address.");
            return;
        }

        // Check password length
        if (formValues.password.length < 8) {
            alert("Password must be at least 8 characters long.");
            return;
        }
        const payload = {
            nom: formValues.nom,
            prenom: formValues.prenom,
            adresse: formValues.adresse,
            num_tel: formValues.telephone,
            email: formValues.email,
            password: formValues.password,
        }
        try {
            const result = await httpClient.post('login_register/register', payload)
            alert('Inscription réussie')
            router.push('/auth/login')
        } catch (e) {
            alert(`Error pendant l'inscription : ${e?.detail}`)
        }
    };

    return (
        <>
            <div className="flex justify-center w-full">
                <div className="w-1/3">
                    <h2>Register</h2>
                    <form className="flex max-w-md flex-col gap-4" onSubmit={handleSubmit}>
                        <div>
                            <div className="mb-2 block">
                                <Label htmlFor="nom" value="Votre nom"/>
                            </div>
                            <TextInput id="nom" name="nom" type="text" placeholder="Votre nom" required/>
                        </div>
                        <div>
                            <div className="mb-2 block">
                                <Label htmlFor="prenom" value="Votre prenom"/>
                            </div>
                            <TextInput id="prenom" name="prenom" type="text" placeholder="Votre prenom" required/>
                        </div>
                        <div>
                            <div className="mb-2 block">
                                <Label htmlFor="telephone" value="Votre telephone"/>
                            </div>
                            <TextInput id="telephone" name="telephone" type="text" placeholder="Votre telephone"
                                       required/>
                        </div>
                        <div>
                            <div className="mb-2 block">
                                <Label htmlFor="adresse" value="Adresse postale"/>
                            </div>
                            <Textarea id="adresse" name="adresse" placeholder="Votre adresse postale" required/>
                        </div>
                        <div>
                            <div className="mb-2 block">
                                <Label htmlFor="email" value="Votre email"/>
                            </div>
                            <TextInput id="email" name="email" type="email" placeholder="name@gmail.com" required/>
                        </div>
                        <div>
                            <div className="mb-2 block">
                                <Label htmlFor="password" value="Your password"/>
                            </div>
                            <TextInput id="password" name="password" type="password" required/>
                        </div>
                        <Button type="submit">Submit</Button>
                    </form>
                </div>
            </div>
        </>
    );
}
