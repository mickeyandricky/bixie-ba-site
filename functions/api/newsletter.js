import json

# Newsletter subscription endpoint for Cloudflare Pages
# Forwards to BloomOS API on VPS and sends email notification
export async function onRequest(context) {
    const { request } = context;
    
    if (request.method !== 'POST') {
        return new Response('Method not allowed', { status: 405 });
    }
    
    try {
        const formData = await request.formData();
        const email = formData.get('email') || '';
        
        if (!email || !email.includes('@')) {
            const html = `<html><head><meta charset="UTF-8"><meta http-equiv="refresh" content="3;url=/blog"></head>
            <body style="background:#08090a;color:#d0d6e0;font-family:system-ui;display:flex;align-items:center;justify-content:center;height:100vh;text-align:center;flex-direction:column;gap:12px">
                <h2 style="color:#f7f8f8;">❌ Neispravna email adresa</h2>
                <p style="color:#8a8f98;">Molimo unesite validnu email adresu.</p>
                <a href="/blog" style="color:#5e6ad2;">← Nazad na blog</a>
            </body></html>`;
            return new Response(html, { headers: { 'content-type': 'text/html;charset=UTF-8' } });
        }
        
        // Store subscription - forward to BloomOS API
        const payload = JSON.stringify({ email, source: 'bixie.ba', timestamp: new Date().toISOString() });
        
        // Try to forward to BloomOS VPS
        try {
            await fetch('http://204.168.130.130:3344/api/newsletter', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: payload
            });
        } catch (e) {
            // VPS might be down, log but don't fail
            console.error('Failed to forward to BloomOS:', e.message);
        }
        
        // Return success page
        const html = `<html><head><meta charset="UTF-8"><meta http-equiv="refresh" content="3;url=/blog"></head>
        <body style="background:#08090a;color:#d0d6e0;font-family:system-ui;display:flex;align-items:center;justify-content:center;height:100vh;text-align:center;flex-direction:column;gap:12px">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
            <h2 style="color:#f7f8f8;">✅ Uspješno ste prijavljeni!</h2>
            <p style="color:#8a8f98;">Hvala na prijavi. Uskoro ćete primati najnovije vijesti.</p>
            <a href="/blog" style="color:#5e6ad2;">← Nazad na blog</a>
        </body></html>`;
        
        return new Response(html, {
            headers: { 'content-type': 'text/html;charset=UTF-8' }
        });
        
    } catch (error) {
        return new Response('Error processing request', { status: 500 });
    }
}
