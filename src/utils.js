function scrollToAnchor(id, offset = 0) {
    const el = document.getElementById(id)
    if (!el) return
  
    const y = el.getBoundingClientRect().top + window.scrollY - offset
    window.scrollTo({ top: y, behavior: 'smooth' })
  }
  
async function getUseCases() {
    const response = await fetch('/src/use-cases.json', { cache: 'no-cache' });
    if (!response.ok) return {};
    return await response.json();
}

async function getUseCaseCategories() {
    const useCasesRecord = await getUseCases();
    const categories = Object.values(useCasesRecord)
        .map(item => item && item.category)
        .filter(Boolean);
    return Array.from(new Set(categories));
}