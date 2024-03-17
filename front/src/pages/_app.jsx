// "use client"
import '@/styles/globals.css';
import Link from 'next/link';
import {Navbar} from 'flowbite-react';

export default function MyApp({Component, pageProps}) {
    return (
        <div className={"container"}>
            <Navbar fluid rounded>
                <Navbar.Brand as={Link} href="#">
                    <img
                        src="https://upload.wikimedia.org/wikipedia/fr/thumb/0/0c/Logo_ISTY.svg/1280px-Logo_ISTY.svg.png"
                        className="mr-3 h-6 sm:h-9" alt="Logo"/>
                    <span
                        className="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Projet Service</span>
                </Navbar.Brand>
                <Navbar.Toggle/>
                <Navbar.Collapse>
                    <Navbar.Link href="/auth/login">Login</Navbar.Link>
                    <Navbar.Link href="/auth/register">Register</Navbar.Link>
                    <Navbar.Link href="/request">Demander un pret</Navbar.Link>
                </Navbar.Collapse>
            </Navbar>
            <div className={"m-6"}>
                <Component {...pageProps} />
            </div>
        </div>
    );
}
