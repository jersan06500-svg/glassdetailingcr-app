// La app ya no usa este service worker. Este archivo borra el caché viejo
// de los celulares que tenían la versión anterior y se da de baja solo.
self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", e => {
  e.waitUntil(
    caches.keys()
      .then(ks => Promise.all(ks.map(k => caches.delete(k))))
      .then(() => self.registration.unregister())
      .then(() => self.clients.matchAll())
      .then(cs => cs.forEach(c => c.navigate(c.url)))
  );
});
