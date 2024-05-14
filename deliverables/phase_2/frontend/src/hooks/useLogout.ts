import { useRouter } from 'next/router';
import { createClient } from "@/utils/supabase/client";  // Supondo que você tenha uma versão client-side da criação de cliente Supabase

export function useLogout() {
    const router = useRouter();
    const supabase = createClient();

    const logout = async () => {
        const { error } = await supabase.auth.signOut();
  
        if (error) {
            // Handle error, possibly show a message to the user
            console.error('Logout failed:', error.message);
        } else {
            // Optionally, revalidate the cache if needed
            // await someMethodToRevalidateCache();

            // Redirect to the homepage or login page
            router.push('/');
        }
    };

    return logout;
}
