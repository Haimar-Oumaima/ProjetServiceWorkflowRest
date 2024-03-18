"use client"
import {Button, Label, Textarea, TextInput} from "flowbite-react";
import httpClient from "@/services/httpClient";
import {useRouter} from "next/router";

export default function Login() {
    const router = useRouter()
    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        const formValues = {};

        for (let [key, value] of formData.entries()) {
            formValues[key] = value;
        }
        const payload = {
            email: formValues.email,
            password: formValues.password,
        }
        let result
        try {
            result = await httpClient.post('login_register/login', payload)
        } catch (e) {
            console.error("cnx refused", e.detail)
            alert(`Error connexion ${e.detail}`)

        }
        const access_token = result?.access_token
        if (access_token) {
            alert("Vous etes connecté")
            sessionStorage.setItem('token', access_token)
            router.push('/request')
        }
    };

return (
    <div className="flex justify-center w-full">
        <div className="w-1/3">
            <h2>Login</h2>
            <form className="flex flex-col gap-4" onSubmit={handleSubmit}>
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
);

}
