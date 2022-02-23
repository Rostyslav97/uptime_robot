import asyncio
from contextlib import suppress
from datetime import datetime
from typing import Optional

from httpx import AsyncClient, Timeout

from core.models import Report, ReportStatuses, Website


class Checker:
    @property
    def websites(self):
        return Website.objects.all()

    async def generate_report(self, site: Website, time: datetime) -> Report:
        async with AsyncClient(timeout=Timeout(2, read=None)) as client:
            with suppress(Exception):
                response = await client.get(url=str(site.url))

                if response.status_code < 300:
                    return Report(
                        site=site,
                        status=ReportStatuses.AVAILABLE.value,
                        created_at=time,
                    )
                elif response.status_code < 500:
                    return Report(
                        site=site,
                        status=ReportStatuses.BLOCKED.value,
                        created_at=time,
                    )

            return Report(
                site=site,
                status=ReportStatuses.NOTAVAILABLE.value,
                created_at=time,
            )

    def save_reports(self, reports: tuple[Report]) -> tuple[Report]:
        objects = Report.objects.bulk_create(reports)
        return objects

    def generate_reports(self):
        now = datetime.now()

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop = asyncio.get_event_loop()

        tasks = [self.generate_report(site, now) for site in self.websites]
        reports: tuple[Report] = loop.run_until_complete(
            asyncio.gather(*tasks),
        )
        loop.close()

        self.save_reports(reports)

        print(">>> DONE")