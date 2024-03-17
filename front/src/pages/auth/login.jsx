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
            console.error("cnx refused")
        }
        const {access_token} = result
        if (access_token) {
            sessionStorage.setItem('token', access_token)
            router.push('/request/submit')
        }
    };

    return (
        <>
            <h2>Login</h2>
            <form className="flex max-w-md flex-col gap-4" onSubmit={handleSubmit}>
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
        </>
    );
}
