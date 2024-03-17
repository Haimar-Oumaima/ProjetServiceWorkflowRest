import {useEffect} from "react";
import {useRouter} from "next/router";

export default function Logout(){
    const router = useRouter()
    useEffect(() => {
        sessionStorage.removeItem('token')
        router.push('/auth/login')
    }, []);
}