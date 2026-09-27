'use client'

import { useEffect, useState } from 'react'
import { supabase } from '@/lib/supabase'

export default function Home() {
  const [status, setStatus] = useState('Testing...')

  useEffect(() => {
    async function testConnection() {
      const { error } = await supabase
        .from('test_locations')
        .select('*')
        .limit(1)

      if (error) {
        setStatus(`❌ Supabase error: ${error.message}`)
      } else {
        setStatus('✅ Supabase connection works!')
      }
    }

    testConnection()
  }, [])

  return (
    <main>
      <h1>{status}</h1>
    </main>
  )
}