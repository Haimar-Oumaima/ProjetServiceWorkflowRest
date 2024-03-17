const million = require('million/compiler');
/** @type {import('next').NextConfig} */

const nextConfig = {
    images: {
        remotePatterns: [
            {
                protocol: 'https',
                hostname: '**',
            },
        ],
    },
    async rewrites() {
        return {
            fallback: [{ source: '/:path*', destination: '/user/:path*' }],
        };
    },
};

const millionConfig = {
    auto: true, // if you're using RSC: auto: { rsc: true },
};

module.exports = million.next(nextConfig, millionConfig);
