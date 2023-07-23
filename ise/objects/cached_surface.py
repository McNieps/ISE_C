import pygame

from ise.app.resource import Resource


class CachedSurface(pygame.Surface):
    def __init__(self,
                 base_surface: pygame.Surface,
                 caching_size: int = None) -> None:

        super().__init__(base_surface.get_size())
        self.fill((255, 0, 0))

        if not Resource.data["engine"]["surface"]["caching_enabled"]:
            raise RuntimeError("Surface caching is not enabled.")

        if caching_size is None:
            caching_size = Resource.data["engine"]["surface"]["caching_size"]

        self._caching_size = caching_size
        self._caching_step = 360 / self._caching_size
        self.surfaces = []

        for i in range(caching_size):
            self.surfaces.append(pygame.transform.rotate(base_surface, i * self._caching_step))

    def _get_surface_index(self,
                           angle: float) -> int:

        return round(angle % 360 / self._caching_step)

    def __getitem__(self, item):
        return self.surfaces[self._get_surface_index(item)]
